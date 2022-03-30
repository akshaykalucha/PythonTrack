from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://instagram.com/aksxayy')

# driver.quit()

print("hello world")