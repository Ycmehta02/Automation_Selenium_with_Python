import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait

opt = Options()
opt.add_argument("--disable-blink-features=AutomationControlled")
# opt.add_argument("--no-sandbox")
# opt.add_argument("--disable-infobars")
# opt.add_argument("--disable-dev-shm-usage")
# opt.add_experimental_option("excludeSwitches", ["enable-automation"])
# opt.add_experimental_option("useAutomationExtension", False)


# Set up WebDriver
serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=opt)
driver.implicitly_wait(20)

# Open the target website
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASSHykoSf1IfZG__UOn2ThyDEK83DOTPmxhzLNxuZ_OEsspBP_1AlguAVsTPTuvs7NQHUB7nMKdNOA&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-568233945%3A1739173274751619&ddm=1")
driver.maximize_window()

#Entering Email and Clicking 'Next'
email_tb = driver.find_element(By.XPATH,"//input[@id='identifierId']")
email_tb.send_keys("riap1330@gmail.com")
driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
time.sleep(5)

#Entering Password and Click 'Next'
pwd_tb = driver.find_element(By.XPATH,"//input[@name='Passwd']")
pwd_tb.send_keys("Abc@556466")
pwd_btn= driver.find_element(By.XPATH,"//span[normalize-space()='Next']")
pwd_btn.click()
time.sleep(10)
print("Email Login Passed")

#Searching "Alian Hub have sent you an invitation" in Search textbox
search =driver.find_element(By.XPATH,"//input[@placeholder='Search mail']")
search.send_keys("Alian Hub have sent you an invitation")
search.send_keys(Keys.RETURN)
time.sleep(10)

#First Mail
mail = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div[2]/div[6]/div[1]/div/table/tbody/tr[1]/td[6]/div/div/div[2]/span/span/span[1]")
mail.click()
time.sleep(10)

#Clicking on link in Mail
e_link = driver.find_element(By.XPATH,"//a[normalize-space()='Click here to Join']")
e_link.click()

#Switch to Alian hub
driver.switch_to.window(driver.window_handles[-1])
time.sleep(10)

##Register----------------------------------------------
# #First Name
# f_name = driver.find_element(By.XPATH,"//input[@id='firstName']")
# f_name.send_keys("Yashvi")
#
# #Last Name
# l_name = driver.find_element(By.XPATH,"//input[@id='lastName']")
# l_name.send_keys("Mehta")
#
# #Enter Password
# pwd = driver.find_element(By.XPATH,"//input[@id='password']")
# pwd.send_keys("Abc@223133")
#
# #Confirm password
# c_pwd = driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
# c_pwd.send_keys("Abc@223133")
#
# #terms and condition
# driver.find_element(By.XPATH,"//span[contains(text(),'I agree to the')]").click()
# time.sleep(10)
#
# btn = driver.find_element(By.XPATH,"//button[normalize-space()='Register']")
# btn.click()
# time.sleep(20)
#
# print("Registered")

##Login-------------------------------------------------------
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']")
# time.sleep(5)

#Email
log_email = driver.find_element(By.XPATH,"//input[@id='email']")
log_email.send_keys("riap1330+104@gmail.com")
#Password
log_pwd = driver.find_element(By.XPATH,"//input[@id='password']")
log_pwd.send_keys("Abc@223133")

#Login buttton
log_btn = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
log_btn.click()
time.sleep(10)

print("Test Case Passed!")








