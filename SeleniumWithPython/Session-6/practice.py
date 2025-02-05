#Test Case
# Open the URL- https://katalon-demo-cura.herokuapp.com/
# Click on the make appointment button
# Verify that URL Changes - assert
# time.sleep (3)
# Enter the username, password
# Next page verify the current URL
# Make appointment text on the web page.

###-------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service= serv)
#
#
# driver.get("https://katalon-demo-cura.herokuapp.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='btn-make-appointment']").click()
#
# #URL Check
# expURL = "https://katalon-demo-cura.herokuapp.com/profile.php#login"
# actURL = driver.current_url
# assert actURL == expURL, "URL not matched"
#
# time.sleep(3)
#
# #entering username
# username = driver.find_element(By.XPATH,"//*[@id='txt-username']")
# username.send_keys("John Doe")
#
# #entering password
# pwd = driver.find_element(By.XPATH,"//*[@id='txt-password']")
# pwd.send_keys("ThisIsNotAPassword")
#
# #clicking Log in
# driver.find_element(By.XPATH,"//*[@id='btn-login']").click()
#
# #URL Check
# expURL2 = "https://katalon-demo-cura.herokuapp.com/#appointmen"
# actURL2 = driver.current_url
# assert actURL2 == expURL2, f"URL not matched {driver.current_url}"

#Make Appointment Text verification
mk_ap= driver.find_element(By.XPATH,"//h2[text()='Make Appointment']")
assert mk_ap.text == 'Make Appointment', "Heading not matched{mk_ap.text}"
print("We reached Section:",mk_ap.text)
print("Test case passed")
