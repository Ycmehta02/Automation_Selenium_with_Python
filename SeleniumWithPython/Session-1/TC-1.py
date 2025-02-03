# Test Case:
# 	1) Open Web Browser(Chrome/firefox/Edge).
# 	2) Open URL https://opensource-demo.orangehrmlive.com/
# 	3) Enter username (Admin).
# 	4) Enter password (admin123).
# 	5) Click on Login.
# 	6) Capture title of the home page. (Actual title)
# 	7) Verify title of the page: OrangeHRM  (Expected)
# 	8) Close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#driver is object of chrome class
#r for "raw string" or use "\\" in location URL
# Define the path to the ChromeDriver
chrome_driver_path = r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Create a Service object
service = Service(chrome_driver_path)

# Pass the Service object to WebDriver
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(10)
#send_keys - inputs the data to field
#find elements using By.NAME
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']" ).click()
#does not have a name use:
#driver.find_element(By.XPATH, "//button[text()=' Login ']").click() #--locate text
#   OR
#driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
#   OR
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
# #--Locate by type="submit"


act_title= driver.title
exp_title= "OrangeHRM"
if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

input("Press Enter to exit and close the browser...")
driver.quit()

