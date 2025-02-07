import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(5)

outframe= driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outframe)

inframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")

driver.switch_to.parent_frame() #switch to outer iframe
ele = driver.find_element(By.XPATH,"//h5[normalize-space()='Nested iFrames']")
print(ele.text)

driver.switch_to.default_content()
print("Back to main page")

