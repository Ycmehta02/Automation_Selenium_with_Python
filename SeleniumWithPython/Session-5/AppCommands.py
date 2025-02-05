from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

#opening the application url
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(5)
#gives title of webpage
print(driver.title)

#gives current url of the webpage
print(driver.current_url)

#source code of the page
print(driver.page_source)


