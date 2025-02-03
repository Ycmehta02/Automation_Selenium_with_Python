from webbrowser import Chrome
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window() #maximize the web browser window
driver.implicitly_wait(10)
#ID Locator
driver.find_element(By.ID,"small-searchterms").send_keys("HP Spectre XT Pro UltraBook")
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
driver.implicitly_wait(10)
#
# #Name Locator
# driver.find_element(By.NAME,"q").send_keys("Nokia Lumia 1020")

# driver.implicitly_wait(10)
# driver.back() #goes to previous page
driver.back() #previous page
driver.implicitly_wait(20)

#LinkText
driver.find_element(By.LINK_TEXT,"Register").click()
# #Partial LinkText
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

driver.implicitly_wait(10)
driver.back()

input("Press Enter to exit and close the browser...")
driver.quit()
