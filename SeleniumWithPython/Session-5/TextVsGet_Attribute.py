from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://demo.nopcommerce.com/login/")

driver.implicitly_wait(10)
driver.maximize_window()

# ele = driver.find_element(By.XPATH,"//*[@id='Email']")
# ele.clear()
# ele.send_keys("abc@gmail.com")
# print("Text: ",ele.text) # blank
# print("get_Attribute:",ele.get_attribute('value')) #value printed (attribute)

#Text is Text value of element (inner text)
#get_attributes gets the value(attribute) of the element

btn = driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print(btn.text) #Log in
print(btn.get_attribute('value')) #blank
print(btn.get_attribute('type')) #submit


