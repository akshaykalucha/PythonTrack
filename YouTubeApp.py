from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from fake_useragent import UserAgent
import json 
import os


options = Options()
options.add_argument('--headless')
# options.add_argument('--window-size=1920,1080')
# ua = UserAgent()
# userAgent = ua.random
# options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# name = input("Enter the username you want to reach: ")

def getYTInfo(name):
    userDict = {}

    URL = f"https://youtube.com/c/{name}"

    driver.get(URL)

    time.sleep(4)



    # time.sleep(5)
    driver.quit()
    print("hello world")

    # Serialization 
    json_object = json.dumps(userDict, indent = 4) 
    return json_object