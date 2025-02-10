# ○ CTRL + A
# ○ CTRL + C
# ○ TAB
# ○ CTRL + V
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

tb1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
tb2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

tb1.send_keys("Hello !!!")

#Keyboard Actions
act = ActionChains(driver)

##tb1 --> Ctrl+A - Select the text

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #Ctrl +A

##tb1--> Ctrl+C - Copy text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() #Ctrl + C

## Press TAB key to navigate to tb2
act.send_keys(Keys.TAB).perform() #TAB

##tb2 --> Ctrl+v Paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #Ctrl + V

time.sleep(5)




