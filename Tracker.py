import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time


URL = 'https://www.flipkart.com/zotac-nvidia-gaming-geforce-gtx-1660ti-twin-fan-6-gb-gddr6-graphics-card/p/itmfdykqwhjh33jf'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

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


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('akshaykalucha3@gmail.com', 'qnozqcbaxjcvqtli')

    subject = 'Price fell down'
    body = (f"Check the graphics card price: {URL}")

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'akshaykalucha3@gmail.com',
        'akshaykalucha@gmail.com',
        msg
    )
    print('Hey email sent')

    server.quit


check_price()

schedule.every(5).seconds.do(check_price)

while True:
    schedule.run_pending()
    time.sleep(1)