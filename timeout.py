import time
from itertools import count
from multiprocessing import Process
import requests
import threading
import json

class perpetualTimer():
    
   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = threading.Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = threading.Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()





def Callback(*args):
    # t = threading.Timer(3, Callback)
    r = requests.get('http://127.0.0.1:5000/', auth=('user', 'pass'))
    r.headers['content-type']
    data = r.json()
    type = data['Type']
    print(type)

t = perpetualTimer(2,Callback)
if __name__ == "__main__":  
    t.start()