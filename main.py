from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(exceutable_path='chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com')

# Waiting for the search bar to load for 5 seconds
# If it doesn't load in 5 seconds, then it will raise an error
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

# Finding the search bar
# and typing 'Hello World' 
# and then pressing Enter
inputElement = driver.find_element(By.CLASS_NAME, 'gLFyf')
# Clearing the input field
inputElement.clear()
inputElement.send_keys('Hello World' + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '"Hello, World!" program')))

# Allows us to click on the first link that appears with the text '"Hello, World!" program'
link = driver.find_element(By.PARTIAL_LINK_TEXT, '"Hello, World!" program')
link.click()

# To find multiple elements we can use the find_elements method

time.sleep(10)

driver.quit()