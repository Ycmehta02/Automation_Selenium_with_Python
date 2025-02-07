import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://practice-automation.com/form-fields/")
driver.maximize_window()

#1) select specific checkbox from list
# ele = driver.find_element(By.XPATH,"//input[@type='checkbox' and contains(@id,'drink')]").click()

#2) Select all the checkbox
ele = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'drink')]")
print(len(ele)) #5

# #Approach1
# for i in range(len(ele)):
#     ele[i].click()

# #Approach2
# for e in ele:
#     e.click()

#3) Select multiple checkboxes by choice

# for e in ele:
#     drink =e.get_attribute('id')
#     if drink == 'drink2' or drink =='drink3':
#         e.click()

# #4) Select last 2 checkbox
# #range(3,5) -->4,5
# #totalnumberofelements-2 = starting index
# for i in range(len(ele)-2,len(ele)):
#     ele[i].click()

# #5) Select first 2 checkboxes
# for i in range(len(ele)):
#     if i<2:
#         ele[i].click()

time.sleep(5)
#6) Clear all checkboxes
for e in ele:
    if e.is_selected():
        e.click()









