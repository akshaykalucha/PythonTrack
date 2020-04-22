from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from secrets import username, password, status

class Twitter():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://twitter.com/login')

        sleep(5)

        #Username is pulled from secrets.py file
        email_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        email_in.send_keys(username)

        #Username notification
        print('Username entered')
 
        #Wait 10 seconds to avoid the typing biomatics trigger 
        sleep(10)

        #Password is pulled from the secrets.py file
        pw_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        pw_in.send_keys(password)

        #Password notification
        print('Password entered')

        #Wait 10 seconds to avoid the typing biomatics trigger 
        sleep(3)

        #Login in button
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span')
        login_btn.click()

        #Successful log
        print('Successful twitter log in')

        #wait 10 seconds 
        sleep(3)

        #Redirect to compose bar page
        # self.driver.get('https://twitter.com/compose/tweet')

        #wait 5 seconds
        sleep (5)
        
        #Twitter Compose 
        print('Twitter composer / Tweet successfuly loaded')

        #Tweet something :D
        whatsHappening_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div')
        whatsHappening_in.send_keys(status)

        #wait 10 seconds
        sleep(5)

        #Tweet Button
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div')
        login_btn.click()

        #Tweet Successful
        print('Tweet Successful')


print('Twitter Script has started')

bot = Twitter()
bot.login()