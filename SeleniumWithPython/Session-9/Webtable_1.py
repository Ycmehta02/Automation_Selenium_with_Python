##-------------Static Table---------------------------------------------

#1) Count number of rows & columns
#2) Read specific row & column data
#3) Read all the rows & columns data
#4) Read date based on conditions (List book name whose author is Mukesh)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1) Count number of rows & columns

rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(rows)
columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th"))
print(columns)

#2) Read specific row & column data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

#3) Read all the rows & columns data
print("All Row & Columns data-->")

for r in range(2,rows+1):
    for c in range(1,columns+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='        ')
    print()

#4) Read date based on conditions (List book name whose author is Mukesh)

for r in range(2,rows):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == "Mukesh":
        book =driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(book, "---Location:",r)
















