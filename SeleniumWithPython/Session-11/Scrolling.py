import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# #1.Scroll Down page by pixel
# driver.execute_script("window_scrollBy(3000)","")
# value = driver.execute_script("return window.pageYOffset;") #current position
# print("Location: ",value)

# #2.Scroll Down page till element is visible
# ele = driver.find_element(By.XPATH,"//input[@id='comboBox']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# value = driver.execute_script("return window.pageYOffset;") #current position
# print("Location: ",value)

#3. Scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;") #current position
print("Location: ",value)
time.sleep(5)

#4. Scroll up to the starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;") #current position
print("Location: ",value)
time.sleep(5)
