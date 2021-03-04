from utils.media_sender import ImageSender
import requests, urllib
import config

def getwords(doc):
    splitter = re.compile('\\W*')
    
    # Split the words by non-alpha characters
    words = [s.lower() for s in splitter.split(doc)
               if len(s)>2 and len(s)<20]
    
    # Return the unique set of words only
    return dict([(w,1) for w in words])

def sampletrain(cl):
    cl.train('Nobody owns the water.','good')
    cl.train('the quick rabbit jumps fences','good')
    cl.train('buy pharmaceuticals now','bad')
    cl.train('make quick money at the online  casino','bad')
    cl.train('the quick brown fox jumps','good')

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