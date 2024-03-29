from typing import Any, List, Tuple

import numpy as np
import pandas as pd
import torch
import torch_geometric as tg
from flamingo.features.featurizer import generate_fingerprints
from torch.utils.data import Dataset

from .graph.molecular_graph import create_molecular_graph_data


def main():
    """Parse the command line arguments and call the modeller class."""
    parser = argparse.ArgumentParser(description="modeller -i input.yml")
    # configure logger
    parser.add_argument('-i', required=True,
                        help="Input file with options")
    parser.add_argument("-m", "--mode", help="Operation mode: train or predict",
                        choices=["train", "predict"], default="train")
    parser.add_argument("--restart", help="restart training", action="store_true", default=False)
    parser.add_argument('-w', help="workdir", default=".")
    args = parser.parse_args()


class FingerprintsDataset(Dataset):
    """Read the smiles, properties and compute the fingerprints."""

    def __init__(
            self, data: pd.DataFrame, properties: str, type_fingerprint: str,
            fingerprint_size: int) -> None:
        """Generate a dataset using fingerprints as features."""
        self.molecules = data['molecules']
        labels = data[properties].to_numpy(np.float32)
        size_labels = len(self.molecules)
        self.labels = torch.from_numpy(labels.reshape(size_labels, len(properties)))
        fingerprints = generate_fingerprints(
            self.molecules, type_fingerprint, fingerprint_size)
        np.save("fingerprints", fingerprints)
        self.fingerprints = torch.from_numpy(fingerprints)

    def __len__(self) -> int:
        """Return dataset length."""
        return self.labels.shape[0]

    def __getitem__(self, idx: int) -> Tuple[Any, Any]:
        """Return the idx dataset element."""
        return self.fingerprints[idx], self.labels[idx]


class MolGraphDataset(tg.data.Dataset):
    """Dataset for molecular graphs."""

    def __init__(self, root: str, data: pd.DataFrame, properties: List[str] = None):
        """Generate Molecular graph dataset."""
        super().__init__(root)
        self.molecules = data['molecules']
        self.molecules.reset_index(drop=True, inplace=True)
        self.norm = tg.transforms.NormalizeFeatures()
        if properties is not None:
            self.labels = data[properties].to_numpy(np.float32)
        else:
            self.labels = None

    def _download(self):
        pass

    def _process(self):
        pass

    def __len__(self):
        """Return dataset length."""
        return len(self.molecules)

    def __getitem__(self, idx):
        """Return the idx dataset element."""
        if self.labels is not None:
            # labels = torch.Tensor([self.labels[idx]]).reshape(1, 1)
            labels = torch.Tensor([self.labels[idx]])
        else:
            labels = None
        data = create_molecular_graph_data(self.molecules[idx], labels)
        return self.norm(data)

#USER SCHEMA VALIDATION

SCHEMA_OPTIMIZER = Schema({

    Optional("name", default="sgd"): any_lambda(("adam", "sgd")),

    # Learning rate
    Optional("lr", default=0.1): float,

    # Momentum
    Optional("momentum", default=0): float,

    # Nesterov accelerated gradient
    Optional("nesterov", default=False): bool

})


TORCH_DEFAULTS = SCHEMA_TORCH.validate({})


SCHEMA_MODEL = Schema({
    # Model's name
    "name": str,
    # Parameters to feed the model
    Optional("parameters", default={}): dict,
})


SCHEMA_FINGERPRINTS = Schema({
    Optional("fingerprint", default='atompair'): any_lambda(('morgan', 'atompair', 'torsion')),
    Optional("nbits", default=2048): int
})

SCHEMA_GRAPH = Schema({
    "molecular_graph": dict
})

SCHEMA_MODELER = Schema({
    # Load the dataset from a file
    "dataset_file": str,

    # Property to predict
    "properties": [str],

    # Method to get the features
    "featurizer": Or(SCHEMA_FINGERPRINTS, equal_lambda("molecular_graph")),

    # Whether to use CPU or GPU
    Optional("use_cuda", default=False): bool,

    Optional("model", default={}): SCHEMA_MODEL,

    Optional("scale_labels", default=True): bool,

    # Sanitize smiles
    Optional("sanitize", default=False): bool,

    # Network and training options options
    Optional("torch_config", default=TORCH_DEFAULTS): SCHEMA_TORCH,

    # File to save the models
    Optional("model_path", default="swan_models.pt"): str,

    # File to save the scales for the features
    Optional("model_scales", default="model_scales.pkl"): str,

    # Workdir
    Optional("workdir", default="."): str
})


DEFAULT_MODELS = {
    "fingerprintfullyconnected": FingerprintFullyConnected,
    "mpnn": MPNN,
}


def select_model(opts: Options) -> nn.Module:
    """Select a model using the input provided by the user."""
    name = opts.name.lower()
    model = DEFAULT_MODELS.get(name, None)
    if model is None:
        raise RuntimeError(f"Model {name} is not None")

    return model(**opts.parameters)

PathLike = Union[str, Path]


def equal_lambda(name: str):
    """Create an schema checking that the keyword matches the expected value."""
    return And(
        str, Use(str.lower), lambda s: s == name)


def any_lambda(array: Iterable[str]):
    """Create an schema checking that the keyword matches one of the expected values."""
    return And(
        str, Use(str.lower), lambda s: s in array)

class FingerprintModeller(Modeller):
    """Object to create models using fingerprints."""

    def create_data_loader(self, indices: np.ndarray) -> DataLoader:
        """Create a DataLoader instance for the data."""
        dataset = FingerprintsDataset(
            self.data.loc[indices], self.opts.properties,
            self.opts.featurizer.fingerprint,
            self.opts.featurizer.nbits)

        return DataLoader(
            dataset=dataset, batch_size=self.opts.torch_config.batch_size)
    def sanitize_data(self):
        """Check that the data in the DataFrame is valid."""
        # discard nan values
        self.data.dropna(inplace=True)

        # Create conformers
        self.data['molecules'].apply(lambda mol: AllChem.EmbedMolecule(mol))

        # Discard molecules that do not have conformer
        LOGGER.info("Removing molecules that don't have any conformer.")
        self.data = self.data[self.data['molecules'].apply(lambda x: x.GetNumConformers()) >= 1]

    def create_new_model(self):
        """Configure a new model."""
        self.epoch = 0
        self.set_network()
        self.set_optimizer()
        # Scales for the features
        self.path_scales = Path(self.opts.workdir) / "swan_scales.pkl"

        # Reload model from file
        if self.opts.restart or self.opts.mode == "predict":
            self.load_model()

        # Create loss function
        self.loss_func = getattr(nn, self.opts.torch_config.loss_function)()
    def set_network(self) -> None:
        """Select the network to use."""
        self.network = select_model(self.opts.model)
        self.network = self.network.to(self.device)

    def set_optimizer(self) -> None:
        """Select the optimizer."""
        optimizers = {"sgd": torch.optim.SGD, "adam": torch.optim.Adam}
        config = self.opts.torch_config.optimizer
        fun = optimizers[config["name"]]
        if config["name"] == "sgd":
            self.optimizer = fun(self.network.parameters(), lr=config["lr"],
                                 momentum=config["momentum"], nesterov=config["nesterov"])
        else:
            self.optimizer = fun(self.network.parameters(), lr=config["lr"])
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, mode='min', min_lr=0.00001)