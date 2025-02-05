from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/register")

driver.implicitly_wait(10)
driver.maximize_window()

driver.back() #orangehrm
driver.forward() #nopcommerce

driver.refresh()

driver.quit()