import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

time.sleep(5)

#driver.close() #close the first webpage
driver.quit() #closes all window and process related to main one (kills driver)














