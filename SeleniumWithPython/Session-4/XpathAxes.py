from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")


#self
# msg = driver.find_element(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/self::a").text
# print(msg)

# #parent
# msg = driver.find_element(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/parent::td").text
# print(msg)
#
# #child ->   self>ancestor>child
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/child::td")
# print(len(msg))
#
# #ancestor
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr").text
# print(msg)
#
# #descendant
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/descendant::*")
# print(len(msg))

# #following
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/following::*")
# print(len(msg))

driver.implicitly_wait(15)

# #following-sibling
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/following-sibling::tr")
# print(len(msg))

#precedings
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/preceding::*")
# print(len(msg))
# msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/preceding::tr")
# print(len(msg))

#preceding-siblings
msg = driver.find_elements(By.XPATH,"//a[normalize-space()='Aegis Logistics Ltd.']/ancestor::tr/preceding-sibling::tr")
print(len(msg))










