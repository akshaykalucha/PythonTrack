import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time



    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"})
    title = soup.find("span", {"class": "_35KyD6"})
    div = price.string

    print(title.text)
    print(div)


    converted_price = div[0:7]
    k = converted_price.replace(",", "")
    w = k.replace("₹", "")
    converted_price = int(w)

    print('this is converted price', converted_price)

    # if(converted_price > 1000):
    #     send_mail()

    return converted_price



###################################

def checkGCprice1660TI():
    URL = "https://www.amazon.in/Zotac-GeForce-1660-GDDR6-Graphic/dp/B07NMWQXLR/ref=sr_1_1?dchild=1&keywords=1660ti&qid=1592377812&s=computers&sr=1-1"

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    price = soup.find("span", {"id": "priceblock_ourprice"})
    div = price.string
    converted_price = div[1:8]
    k = converted_price.replace(",", "")
    converted_price = int(k)

    return converted_price





def checkGCprice1660SUPER():
    URL = "https://www.amazon.in/GeForce-GTX-1660-OC-Gv-N166SOC-6GD/dp/B07ZPM2BVR"

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    price = soup.find("span", {"id": "priceblock_ourprice"})
    div = price.string
    converted_price = div[1:8]
    k = converted_price.replace(",", "")
    converted_price = int(k)

    return converted_price 


#######################################################


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('senders email', 'g3suitepass')

    subject = 'Price fell down'
    body = (f"Check the graphics card price: {URL}")

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'senders email',
        'reciever email',
        msg
    )
    print('Hey email sent')

    server.quit


# check_price()

# schedule.every(5).seconds.do(check_price)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
