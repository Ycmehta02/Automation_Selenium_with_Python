import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.implicitly_wait(10)

# reg = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Register").send_keys(reg)

#New Tab & Window
driver.get("https://demo.nopcommerce.com/")

driver.switch_to.new_window('tab') #new tab

driver.get("https://www.opencart.com/")

driver.switch_to.new_window('window') #new browser window

driver.get("https//www.orangehrm.com/") #focus will be here



