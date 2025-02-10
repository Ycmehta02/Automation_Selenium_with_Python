import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
box = driver.find_element(By.XPATH,"//div[@id='droppable']")

#Drag N Drop

act = ActionChains(driver)
act.drag_and_drop(ele,box).perform()
