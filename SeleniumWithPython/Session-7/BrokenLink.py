#we need to install requests package through File -->Settings -> ProjectInterpreter --> + -> requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,'a')
count = 0
for l in links:
    url= l.get_attribute('href')
    try:
        res= requests.head(url)
    except:
        None
        
    if res.status_code>=400:
        print(url,"Broken link")
        count+=1
    else:
        print(url,"Valid link")

print("Total",count)














