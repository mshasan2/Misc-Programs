from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(exceutable_path='chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

time.sleep(10)

driver.quit()

# The code above is a simple example of how to use the Selenium library
# to open a browser and navigate to a website.