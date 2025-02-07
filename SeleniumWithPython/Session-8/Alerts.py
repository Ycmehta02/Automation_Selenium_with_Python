import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
ele = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
#normalize-space() is same as text method --but it will ignore additional spaces
ele.click()
time.sleep(5)

#switch to current alert window
alert= driver.switch_to.alert
print(alert.text)

alert.send_keys("Hello fellas!")
alert.accept() #close alert window by OK button
# alert.dismiss() #close alert window by Cancel button





