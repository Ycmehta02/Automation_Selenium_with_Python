import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.implicitly_wait(5) ## for all the driver instance
#opening the application url
driver.get("https://www.google.com/")
driver.maximize_window()

ele = driver.find_element(By.NAME,'q')
ele.send_keys("Selenium")
ele.submit()

#time.sleep(3)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()



