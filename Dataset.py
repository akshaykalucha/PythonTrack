from typing import Any, List, Tuple

import numpy as np
import pandas as pd
import torch
import torch_geometric as tg
from flamingo.features.featurizer import generate_fingerprints
from torch.utils.data import Dataset

from .graph.molecular_graph import create_molecular_graph_data


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

