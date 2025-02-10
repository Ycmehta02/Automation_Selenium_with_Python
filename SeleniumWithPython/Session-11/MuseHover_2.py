import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://practice-automation.com/hover/")
driver.maximize_window()

ele = driver.find_element(By.XPATH,"//h3[@id='mouse_over']")

#Mouse Hover
act = ActionChains(driver)
act.move_to_element(ele).perform()

time.sleep(5)
