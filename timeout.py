import time
from itertools import count
from multiprocessing import Process
import requests
import threading
import json
from MakeTweet import trackTweet

class perpetualTimer():
    
   def __init__(self,t,hFunction,args):
      self.t=t
      self.args = args
      print("thi is is t", self.t)
      self.hFunction = hFunction
      print('this is function passed', self.hFunction)
      self.thread = threading.Timer(self.t,self.handle_function)

   def handle_function(self, *args):
      print("starting passed function....")
      print("these are args to funtion", self.args)
      try:
         self.hFunction(*self.args)
         self.thread = threading.Timer(self.t,self.handle_function, args=self.args)
      except:
         self.hFunction()
         self.thread = threading.Timer(self.t, self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()




def Callback(*args):
   # t = threading.Timer(3, Callback)
   r = requests.get('http://akshaykaluchascriptapp.herokuapp.com/', auth=('user', 'pass'))
   r.headers['content-type']
   data = r.json()
   type = data['Type']
   print(data)
   print(threading.activeCount(), "threads active after callback")


t = None
tracker = None
userTweet = 1270427231131537408
user = "lifeofakshy"
count = 2


def TweetTracker(user, userTweet):
   trackTweet(user, userTweet)
   print("starting tracktweet...")
   print(threading.activeCount(),
    "threads active startTrack")


def startTweetTracker():
   global tracker
   tracker = perpetualTimer(5,
   TweetTracker, args=("lifeofakshy", 1270427231131537408))
   tracker.start()

startTweetTracker()


# WAIT_TIME_SECONDS = 5


# ticker = threading.Event()
# while not ticker.wait(WAIT_TIME_SECONDS):
#     Callback()



def startThread():
   global t
   t = perpetualTimer(5,
   Callback, args=None)
   t.start()

startThread()
   
def cancelThread():
   global t
   t.cancel()
   del t
   print(t)

# if __name__ == "__main__":  
#    t.cancel()