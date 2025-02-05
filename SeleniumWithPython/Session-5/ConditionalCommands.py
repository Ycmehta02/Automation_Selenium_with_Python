from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

#is_displayed()
search = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Displayed: ",search.is_displayed()) #True
#is_enabled()
print("Enabled: ",search.is_enabled()) #True

#is_selected() --for radio button and checkbox
rb_m= driver.find_element(By.XPATH,"//input[@id='gender-male']")
rb_f= driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rb_m.is_selected()) #False
print(rb_f.is_selected()) #False

rb_f.click()

print("After selecting: ")
print(rb_m.is_selected()) #False
print(rb_f.is_selected()) #True


driver.close()

