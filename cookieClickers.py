from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(exceutable_path='chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'promptContentChangeLanguage')))

languageSelector = driver.find_element(By.ID, 'promptContentChangeLanguage')
english_ln = languageSelector.find_element(By.ID, 'langSelect-EN')
english_ln.click()

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, 'bigCookie')))

cookie = driver.find_element(By.ID, 'bigCookie')
cookie.click()

time.sleep(10)

driver.quit()