#Tagname --> Select
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop = driver.find_element(By.XPATH,"//select[@id='country']")
driver.execute_script("arguments[0].scrollIntoView();", drop) #scroll down
dropdown =Select(drop)

time.sleep(5)
#--> select options for the dropdown
dropdown.select_by_visible_text("Canada")
#dropdown.select_by_value("canada")
#dropdown.select_by_index(2) #index--> count manually from select tab(0)


#--> Capture all the options and print them
all_option= dropdown.options #Select class object
print("Total",len(all_option))
for opt in all_option:
    print(opt.text)

#--> Select option from dropdown without using built-in methods
for opt in all_option:
    if opt.text=="Canada":
        opt.click()
        print("Selected :",opt.text)

#if dont want to use select class
options_all= driver.find_elements(By.XPATH,"//*[@id='country']/option") #gives all option
print(len(options_all)) #10








