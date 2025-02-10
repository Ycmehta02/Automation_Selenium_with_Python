import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up WebDriver
serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)

# Open the target website
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Locate the file upload element and upload a file
upload = driver.find_element(By.XPATH, "//input[@id='singleFileInput']")
file_path = r"C:\Users\Alian\Desktop\YM\V Model.png"  # Replace with the actual file path
upload.send_keys(file_path)

# Add a delay to observe the upload process
time.sleep(5)

btn = driver.find_element(By.XPATH,"//button[normalize-space()='Upload Single File']")
btn.click()

txt = driver.find_element(By.XPATH,"//p[@id='singleFileStatus']")
print(txt.text)

time.sleep(5)

# Close the browser
driver.quit()
