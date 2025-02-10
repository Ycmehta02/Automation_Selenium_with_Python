import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//input[@id='field1']")
ele.clear()
ele.send_keys("Double Click!")
btn = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

#Double Click
act = ActionChains(driver)
act.double_click(btn).perform()
