import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//div[@class='dropdown']")
ele1 = driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")

#Mouse Hover

act = ActionChains(driver)
act.move_to_element(ele).move_to_element(ele1).click().perform()
time.sleep(5)
