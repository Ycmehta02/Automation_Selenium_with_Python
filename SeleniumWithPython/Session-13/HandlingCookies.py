import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#captures cookies from browser
#use dictionary object to store one cookie
cookies = driver.get_cookies()
print("Size:",len(cookies))

#print details of all cookies
for c in cookies:
    print(c)
    print(c.get('name'),":",c.get('value'))

#Add new cookie to browser
driver.add_cookie({"name":"MyCookie","value":"12345678"})
cookies =driver.get_cookies() #capture again to get new cookies
print("New Size:",len(cookies))


#delete a specific cookie from browser
driver.delete_cookie("MyCookie")
cookies =driver.get_cookies()
print("New Size:",len(cookies))

#Deleting all cookies
driver.delete_all_cookies()
cookies =driver.get_cookies()
print("New Size:",len(cookies))


time.sleep(5)

driver.close()
