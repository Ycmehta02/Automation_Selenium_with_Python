from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://demo.nopcommerce.com/")

driver.implicitly_wait(10)
driver.maximize_window()

### find_element() -- returns single web element------------------
#
# #1) Locator matching with the single web element
# ele = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# ele.send_keys("Macbook")

# #2) Locator matching with multiple web element
# ele = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(ele.text) #sitemap

# #3) Element not available then throw NoSuchElementException
# ele = driver.find_element(By.LINK_TEXT,"Log_in")
# ele.click() #NoSuchElementException

### find_elements() --Returns multiple web element-------------------

# #1) Locator matching with single web element
# ele = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(ele)) # 1
# ele[0].send_keys("Macbook")

# #2) Locator matching with multiple web element
# ele = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(ele)) #23
# #print(ele[0].text) #Sitemap
# for e in ele:
#     print(e.text)

#3) Element not available
ele = driver.find_elements(By.LINK_TEXT,"Log_in")
print(len(ele)) # 0




