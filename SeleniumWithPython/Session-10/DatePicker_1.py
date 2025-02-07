from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#dd/mm/yyyy
dp1 = driver.find_element(By.XPATH,"//input[@id='datepicker']")
dp1.click()

date = "07"
month = "February"
year = "2025"

#Select Month and Year
while True:
    m =driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    y =driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if m==month and y==year:
        break
    else:
        next = driver.find_element(By.XPATH,"//a[@title='Next']")
        next.click()

#Select Date
dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table//tbody/tr/td/a")
for e in dates:
    if e.text==date:
        e.click()
        break

print("Date picked")
