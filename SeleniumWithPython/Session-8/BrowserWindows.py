import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# win = driver.current_window_handle
# print(win) #F228A9B86CA5A65542459592D5A4BCFD
# #everytime new Id will be created

time.sleep(3)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
winIDs= driver.window_handles


##Approach 1
##----------------------------
# parent = winIDs[0]
# child = winIDs[1]
# #print(parent,child)
#
# driver.switch_to.window(child)
# print("Child Window:",driver.title)
#
# driver.switch_to.window(parent)
# print("Parent Window:",driver.title)

# #Approach 2
# #---------------------------------
# for w in winIDs:
#     driver.switch_to.window(w)
#     print(driver.title)


#Approach 3---close specific window
for w in winIDs:
    driver.switch_to.window(w)
    if driver.title== "OrangeHRM":
        driver.close()
