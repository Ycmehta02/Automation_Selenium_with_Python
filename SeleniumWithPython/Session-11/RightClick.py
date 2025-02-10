import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/3.x/demo.html")
driver.maximize_window()

btn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

#Right Click
act=ActionChains(driver)
act.context_click(btn).perform()
