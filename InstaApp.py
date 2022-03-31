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

def getInfo(name):
    userDict = {}

    URL = "https://instagram.com"

    username = os.environ["username"]
    password = os.environ["password"]

    driver.get(URL)

    time.sleep(4)

    username_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    username_input.send_keys(username)
    password_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password_input.send_keys(password)

    button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    time.sleep(2)
    button.click()
    time.sleep(5)

    driver.get(f'{URL}/{name}')
    time.sleep(3)
    try:
        followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span").get_attribute("title")
        userDict["followers"] = followers
    except:
        userDict["followers"] = None
    try:
        image = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/span/img").get_attribute("src")
        userDict["profileImgSrc"] = image
    except:
        userDict["profileImgSrc"] = None
    try:
        bio = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div").text
        userDict["userBio"] = bio
    except:
        userDict["userBio"] = None

    try:
        bioURL = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/a[1]/div").text
        userDict["bioURL"] = bioURL
    except:
        userDict["bioURL"] = None

    # time.sleep(5)
    driver.quit()
    print("hello world")

    # Serialization 
    json_object = json.dumps(userDict, indent = 4) 
    return json_object