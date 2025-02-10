import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
time.sleep(5)

admin = driver.find_element((By.XPATH,"//a[normalize-space()='']"))
userman = driver.find_element(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab --parent --visited']")
users = driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")

#Hover Action

act = ActionChains(driver)
act.move_to_element(admin).click().move_to_element(userman).click().perform()
act.move_to_element(users).click().perform()



