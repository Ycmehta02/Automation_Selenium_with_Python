from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://automationpractice.com/index.php")
driver.maximize_window() #maximize the web browser window

driver.implicitly_wait(10)

sliders= driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #5 total no of sliders on home page

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #149 total no of links on home page

