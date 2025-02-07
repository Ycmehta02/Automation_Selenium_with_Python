import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://practice-automation.com/iframes/")
driver.maximize_window()

driver.switch_to.frame("top-iframe")
driver.find_element(By.LINK_TEXT,"Get started").click()
driver.switch_to.default_content()#back to main page


driver.switch_to.frame("bottom-iframe")
driver.find_element(By.LINK_TEXT,"Read more")
driver.switch_to.default_content()#back to main page
