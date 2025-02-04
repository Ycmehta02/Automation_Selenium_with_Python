#XPath Options
#https://demo.alianhub.com/#/login

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By


serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver.implicitly_wait(10)
driver.get("https://demo.opencart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#OR operator
#driver.find_element(By.XPATH,"//*[@id='search' or @name='search']/input")

#and operator
#driver.find_element(By.XPATH,"//*[@id='search' and @name='search']/input")

