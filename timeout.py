import time
from itertools import count
from multiprocessing import Process
import requests
import threading
import json
from MakeTweet import trackTweet
from CheckPrices import start_trecking

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


def Callback():
   # t = threading.Timer(3, Callback)
   r = requests.get('http://akshaykaluchascriptapp.herokuapp.com/', auth=('user', 'pass'))
   r.headers['content-type']
   data = r.json()
   # type = data['Type']
   print(data)
   print(threading.activeCount(), "threads active after callback")


t = None
tracker = None
# userTweet = userTweet
# user = "lifeofakshy"
# count = 2


def TweetTracker(user, userTweet):
   try:
      likedTweets = trackTweet(user, userTweet)
      return likedTweets
   except:
      error = "an error occured"
      return error


def startTweetTracker(user, userTweet):
   global tracker
   tracker = perpetualTimer(20,
   TweetTracker, args=(user, userTweet))
   return tracker.start()


def stopTweetTracker():
   global tracker
   tracker.cancel()
   del tracker
   print(tracker)

# startTweetTracker(user=user, userTweet=userTweet)


# WAIT_TIME_SECONDS = 5


# ticker = threading.Event()
# while not ticker.wait(WAIT_TIME_SECONDS):
#     Callback()


crawling = None


def startPCSearch():
   print("Amazon crawling starting......")
   global crawling
   crawling = perpetualTimer(6, start_trecking, args=None)
   crawling.start()


# startPCSearch()

def cancelPCSearch():
   global crawling
   crawling.cancel()
   del crawling

# time.sleep(10)
cancelPCSearch()

def startThread():
   global t
   t = perpetualTimer(300,
   Callback, args=None)
   t.start()

# startThread()
   
def cancelThread():
   global t
   t.cancel()
   del t
   print(t)

# if __name__ == "__main__":  
#    pass