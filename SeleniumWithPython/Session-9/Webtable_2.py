##---------------Dynamic Table------------------------------------------
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

rows = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr"))
print("Rows: ",rows)

for r in range(1,rows+1):
    data = driver.find_element(By.XPATH,"//*[@id='taskTable']//tr["+str(r)+"]/td[3]").text
    print(data)
