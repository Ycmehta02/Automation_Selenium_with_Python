import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://practice-automation.com/popups/")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//button[@id='alert']")
ele.click()

# #direct method
# driver.switch_to.alert.accept()

#extra steps
alert = driver.switch_to.alert
print(alert.text)

#clicks on OK button
alert.accept()