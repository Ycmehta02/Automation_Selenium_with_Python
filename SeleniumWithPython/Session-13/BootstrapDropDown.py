import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up WebDriver
serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

# Open the target website
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@aria-label='Country']").click()
dd = driver.find_elements(By.XPATH,"//*[@id='billing_country']/option")
# [@value='AD']
print(len(dd))
time.sleep(5)

for c in dd:
    if c.text =="Peru":
        c.click()
        break

time.sleep(5)


