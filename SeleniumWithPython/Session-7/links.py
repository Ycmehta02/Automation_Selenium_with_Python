from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

# #-> click on link
# driver.find_element(By.LINK_TEXT,"Digital downloads").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click() #not preferred

#-> find number of links in a page
# links= driver.find_elements(By.TAG_NAME,'a')
links= driver.find_elements(By.XPATH,"//a")
print("Total",len(links))

#print all the link names
for l in links:
    print(l.text)



