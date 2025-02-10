import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source = driver.find_element(By.XPATH,"//div[@id='box5']")
dest = driver.find_element(By.XPATH,"//div[@id='box105']")

#drag N drop

act = ActionChains(driver)
act.drag_and_drop(source,dest).perform()
