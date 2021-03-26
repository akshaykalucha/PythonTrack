from utils.media_sender import ImageSender
import requests, urllib
import config



class EvaluateChoose(object):
    def __init__(self, models_path, configuration_path):
        self.models_path = models_path
        self.configuration_path = configuration_path

    def evaluation(self, validation_data, validation_labels):
        # This function takes validation data and labels and evaluate them
        # Evaluation results are gathered in list which is saved to txt file. This saving is done because of preventing
        # evaluate it every running.
        # Returns results of evaluation which is list of tuples. Each tuple has such shape (model_name, acc, loss).
        results = []

        file = 'results_of_models.json'
        file_path = os.path.join(self.configuration_path, file)
        if os.path.exists(file_path):
            with open(file_path) as results_file:
                results_dict = json.load(results_file)
            results_str = results_dict['results']
            for each in results_str:
                results.append((each[0], float(each[1]), float(each[2])))
            print('Results were loaded from {}!'.format(self.configuration_path))
        else:
            models = os.listdir(self.models_path)
            for each in models[:-3]:
                print('{} model is loaded from the {} folder.'.format(each, self.models_path))
                model_path = os.path.join(self.models_path, each)
                model = tensorflow.keras.models.load_model(model_path)
                loss, acc = model.evaluate(validation_data, validation_labels, verbose=2)
                results.append((each, str(acc), str(loss)))
            results_dict = {'results': results}
            with open(file_path, 'w') as results_file:
                json.dump(results_dict, results_file)
            print('Results were saved to {}!'.format(self.configuration_path))
        return results


    def choose_max(self, validation_data, validation_labels):
        # validation data and validation labels are given as input in order to call evaluation function
        # We get results list and we choose the model which has maximum accuracy
        results = self.evaluation(validation_data, validation_labels)
        max_result = max(results, key=lambda item: item[1])
        print('The best accuracy was obtained from the {}!'.format(max_result[0]))

        return max_result

    def split_return_aug_types(self, model_name):
        # This function is for splitting augmentation types from the model name. It is used in order to make the code
        # run automatically
        temp_name = model_name[:-3]
        delete_index = len('model_')
        result = temp_name[delete_index:]
        aug_types = []

        if 'together' in result:
            aug_types.append(result)
        elif 'without_augmentation' in result:
            aug_types = []
        else:
            if '_' in result:
                aug_types = result.split('_')
            else:
                aug_types.append(result)
        return aug_types

def getwords(doc):
    splitter = re.compile('\\W*')
    
    # Split the words by non-alpha characters
    words = [s.lower() for s in splitter.split(doc)
               if len(s)>2 and len(s)<20]
    
    # Return the unique set of words only
    return dict([(w,1) for w in words])



class BingViews():
    def __init__(self, interface_layer):
        self.image_sender = ImageSender(interface_layer)
        self.routes = [
            ("/i(mage)?\s(?P<term>[^$]+)$", self.bing_image_search)
        ]

    def bing_image_search(self, message, match):
        req = requests.get("https://api.datamarket.azure.com/Bing/Search/v1/Image?Query=%27{}%27&$format=json&$top=1".format(match.group("term")), auth=("",config.bing_api))
        image_url = urllib.unquote(req.json()['d']['results'][0]['MediaUrl'].encode('utf-8'))
        self.image_sender.send_by_url(jid=message.getFrom(), file_url=image_url)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        # Calculate current probability
        basicprob = prf(f,cat)

        # Count the number of times this feature has appeared in 
        # all categories
        totals = sum([self.fcount(f,c) for c in self.categories()])
        
        # Calculate the weighted average
        bp = ((weight * ap) + (totals * basicprob)) / (weight + totals)
        return bp

    def sampletrain(cl):
        cl.train('Nobody owns the water.','good')
        cl.train('the quick rabbit jumps fences','good')
        cl.train('buy pharmaceuticals now','bad')
        cl.train('make quick money at the online  casino','bad')
        cl.train('the quick brown fox jumps','good')

class naivebayes(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.thresholds = {}

    def setthreshold(self,cat,t):
        self.thresholds[cat] = t

    def getthreshold(self,cat):
        if cat not in self.thresholds:
            return 1.0
        return self.thresholds[cat]

    def classify(self, item, default=None):
        # Find the category with the highest probability
        max = 0
        for cat in self.categories():
            cat_prob = self.prob(item, cat)
            # print cat, probs[cat]
            if cat_prob >= max:
                max = cat_prob
                best = cat

        return best
        
        def classify_with_thresholds(self,item,default=None):
            probs={}
        # Find the category with the highest probability
        max=0.0
        for cat in self.categories():
            probs[cat]=self.prob(item,cat)
            #print cat, probs[cat]
            if probs[cat]>max:
                max = probs[cat]
                best = cat
            
        # Make sure the probability exceeds threshold*next best
        for cat in probs:
            if cat == best:
                continue
            if probs[cat]*self.getthreshold(best)>probs[best]:
                return default
        return best


class Member:  # class for member
    def __init__(self, name, profile_url, publications):
        self.name = name
        self.profile_url = profile_url
        self.publications = publications


class IMGpro:  # class for IMG
    def __init__(self, title, summary, PI_name):
        self.title = title
        self.summary = summary
        self.PI_name = PI_name


root = Tk()
root.geometry("1050x500")
root.title("PI Estimator Tool for SEHIR CS Projects")
app = PI_Estimator(root)
root.mainloop()


# Validation data is taken from folders
data_validation, labels_validation = rd_validation.load_augmented_dataset([])
validation_dataset = (data_validation, labels_validation)

# Evaluate and Choose class is declared here

ev_choose = EvaluateChoose(models_path, configuration_path)
maximum_result = ev_choose.choose_max(data_validation, labels_validation)
augmentation_of_max = ev_choose.split_return_aug_types(maximum_result[0])

# Transfer Learning for non-pretrained model 100 epochs

#     unfreezed   weights     trainable
# NP  False       None        True          non pretrained
# PF  False       'imagenet'  False         frozen pretrained
# PD  True        'imagenet'  True          defrosted pretrained

models = {'pre_trained_frozen': [False, 'imagenet', False],
          'unfreezed_pretrained': [True, 'imagenet', True],
          'non_pretrained': [False, None, True]}

epochs = 100
print('VGG16 will be trained in {} combinations on the following dataset: {}.'.format(len(models), augmentation_of_max))
train_data_raw, train_labels_raw = rd_train.load_augmented_dataset(augmentation_of_max)


for each in models.keys():
    model_params = models[each]
    print('Transfer Learning model has chosen as {} version of ResNet'.format(each))
    print('Model parameters will be: Unfreezed: {}, Weights: {}, Trainable: {}'.format(model_params[0], model_params[1],
                                                                                       model_params[2]))

    transfer_learning_model = TransferModel(epochs, input_shape, models_path, defrosted=model_params[0],
                                            weights=model_params[1], trainable=model_params[2])
    history = transfer_learning_model.model(train_data_raw, train_labels_raw, validation_dataset, model_name=each)

    path_image_accuracy = os.path.join(results_path, each + '_accuracy.png')
    path_image_loss = os.path.join(results_path, each + '_loss.png')

    plot_images_results(path_image_accuracy, history, 'accuracy')
    plot_images_results(path_image_loss, history, 'loss')



class fisherclassifier(classifier):
    def cprob(self,f,cat):
        # The frequency of this feature in this category
        clf = self.fprob(f,cat)
        if clf == 0:
            return 0
        
        # The frequency of this feature in all the categories
        freqsum = sum([self.fprob(f,c) for c in self.categories()])
         
        # The probability is the frequency in this category divided by
        # the overall frequency
        p = clf/(freqsum)
        return p

    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.minimums={}    

    def setminimum(self,cat,min):
        self.minimums[cat]=min
      
    def getminimum(self,cat):
        if cat not in self.minimums:
            return 0
        return self.minimums[cat]

    def fisherprob(self,item,cat):
        # Multiply all the probabilities together
        p = 1
        features = self.getfeatures(item)
        for f in features:
            p *= (self.weightedprob(f,cat,self.cprob))
            # Take the natural log and multiply by -2
            fscore = -2*math.log(p)

        # Use the inverse chi2 function to get a probability
        return self.invchi2(fscore,len(features)*2)

    def invchi2(self,chi,df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df//2):
            term *= m / i
            sum += term
        return min(sum, 1.0)

    def classify(self,item,default=None):
        # Loop through looking for the best result
        best = default
        max = 0.0
        for c in self.categories():
            p = self.fisherprob(item,c)
            # Make sure it exceeds its minimum
            if p>self.getminimum(c) and p>max:
                best=c
                max=p
        return best


class Predictor:  # Predictor class for collecting data, training and creating classifier and make prediction
    def __init__(self):
        self.classifier = ""
        self.faculty_members = {}
        self.projects = {}

    def fetch_members(self):  # collects the links to the members profile pages from the first link
        url = app.entry_url_people.get()
        page = urllib2.urlopen(url)
        doc = page.read()
        soup = BeautifulSoup(doc, 'html.parser')
        items = soup.find_all(class_="member")
        links_temp = []
        for i in items:
            for tag in i.find_all('a'):
                links_temp.append(tag.get('href'))
        links = []
        i = 0
        while i < len(links_temp):
            links.append("ht"+links_temp[i])
            i += 3
        return links


            def fetch_publications(self):  # goes to each members profile page and collects all the necessary data
        list_of_members_url = self.fetch_members()
        for member_url in list_of_members_url:
            url = member_url
            page = urllib2.urlopen(url)
            doc = page.read()
            soup = BeautifulSoup(doc, 'html.parser')
            name = soup.find_all('h3')
            name = name[0].text.split()
            name = name[0] + " " + name[-1]
            table = soup.find_all(class_="tab-pane active pubs")
            publications = []
            for item in table:
                for tag in item.find_all("li"):
                    app_item = tag.text.strip()[4:]  # filtering out unwanted info and characters
                    while app_item.startswith('\n'):
                        app_item = app_item[1:]
                    if app_item.endswith("[1\n  Citation]"):
                        app_item = app_item[:-19]
                    elif app_item.endswith("\n  \n  Citations]"):
                        app_item = app_item[:-23]
                        while app_item.endswith('\n'):
                            app_item = app_item[:-1]
                        app_item = app_item
                    publications.append(app_item)
            current_fac_member = FacultyMember(name, member_url, publications)  # crating a faculty member object for adding to database
            self.faculty_members.setdefault(name, current_fac_member)  # adding each member to the database