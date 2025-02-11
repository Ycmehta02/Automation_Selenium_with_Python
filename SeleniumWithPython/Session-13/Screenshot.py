import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.save_screenshot(r"C:\Users\Alian\Desktop\YM_Selenium\SeleniumWithPython\Session-13\homepage.png")

# driver.save_screenshot(os.getcwd()+"\\homepage.png") #current working directory

driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

# driver.get_screenshot_as_base64() #saves ss in binary format
# driver.get_screenshot_as_png()

time.sleep(5)
driver.close()
