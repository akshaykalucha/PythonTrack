import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import threading
import time
  



headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}



class Queue(object):

    def __init__(self):
        self.item = []
    def __repr__(self):
        return "{}".format(self.item)
    def __str__(self):
        return "{}".format(self.item)


    def enque(self, add):
        self.item.insert(0, add)
        return True
    def size(self):
        return len(self.item)
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def deque(self):
        if self.size == 0:
            return None
        else:
            return self.item.pop()




global queue
queue = Queue()

priceList = []


def add_prices(*prices):
    print(sum(prices))
    return sum(prices)






def checkPrice(url):

    global priceList
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("span", {"id": "priceblock_ourprice"})
    div = price.string
    # converted_price = div[1:8]
    k = div.replace(",", "")
    z = k.replace("₹", "")
    w = z.replace(" ", "")
    x = " ".join(w.split())
    price = x.replace(".00", "")
    converted_price = int(price)
    

    souptitle = soup.find("span", {"id": "productTitle"}).text
    title = souptitle.replace('\n', '')
    
    dic = {
        "title": title,
        "price": converted_price
    }
    priceList.append(dic)
    if len(priceList)==5:
        prc = []
        for i in range(len(priceList)):
            prc.append(priceList[i]["price"])
        tup = tuple(prc)
        return returnFunc(), add_prices(*tup)



def returnFunc():
    return priceList

    # print(priceList)
    # queue.enque(priceList)



def start(url):
    thread = threading.Thread(target=checkPrice, args=(url,))
    thread.start()
    # thread.join()

    # while True:
    #     flag = queue.isEmpty()
    #     if flag:
    #         pass
    #     else:
    #         thread.join()
    #         queue.deque()
    #         print(priceList)
    #         break




urlList = ["https://www.amazon.in/Zotac-GeForce-1660-GDDR6-Graphic/dp/B07NMWQXLR",
"https://www.amazon.in/Kingston-Internal-2000MB-SA2000M8-500G/dp/B07VXCFNVS/",
"https://www.amazon.in/gp/product/B07MV9BMNY/",
"https://www.amazon.in/gp/product/B07B4GNMS9/",
"https://www.amazon.in/gp/product/B07STGGQ18/"]



def start_trecking():
    for url in urlList:
        start(url)

start_trecking()