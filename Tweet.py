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

 • /addwhitelist: promotes the user to Whitelist User
 • /removewhitelist: demotes the user from Whitelist User
 
 *Bot Admin Lists:*
 • /whitelistlist - List whitelisted users.
 • /supportlist - List support users.
 • /sudolist - List sudo users.
 • /devlist - List dev users.
"""

SUDO_HANDLER = CommandHandler(("addsudo"), addsudo, pass_args=True)
SUPPORT_HANDLER = CommandHandler(("addsupport"), addsupport, pass_args=True)
WHITELIST_HANDLER = CommandHandler(("addwhitelist"), addwhitelist, pass_args=True)
UNSUDO_HANDLER = CommandHandler(("removesudo"), removesudo, pass_args=True)
UNSUPPORT_HANDLER = CommandHandler(("removesupport"), removesupport, pass_args=True)
UNWHITELIST_HANDLER = CommandHandler(("removewhitelist"), removewhitelist, pass_args=True)

WHITELISTLIST_HANDLER = CommandHandler(["whitelistlist"], whitelistlist)
SUPPORTLIST_HANDLER = CommandHandler(["supportlist"], supportlist)
SUDOLIST_HANDLER = CommandHandler(["sudolist"], sudolist)
DEVLIST_HANDLER = CommandHandler(["devlist"], devlist)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(SUPPORT_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)
dispatcher.add_handler(UNSUDO_HANDLER)
dispatcher.add_handler(UNSUPPORT_HANDLER)
dispatcher.add_handler(UNWHITELIST_HANDLER)

dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)
dispatcher.add_handler(DEVLIST_HANDLER)

