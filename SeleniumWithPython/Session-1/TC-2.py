# Test Case:
# 	1) Open Web Browser(Chrome/firefox/Edge)
# 	2) Open URL https://admin-demo.nopcommerce.com/login
# 	3) Provide Email (admin@yourstore.com).
# 	4) Provide password (admin).
# 	5) Click on Login.
# 	6) Capture title of the dashboard page. (Actual title)
# 	7) Verify title of the page: "Dashboard / nonCommerce administration" (Expected)
# 	8) Close browser


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")

driver.implicitly_wait(10)

email = driver.find_element(By.NAME,"Email")
email.clear()
email.send_keys("admin@yourstore.com")

password = driver.find_element(By.NAME,"Password")
password.clear()
password.send_keys("admin")

driver.find_element(By.NAME,"RememberMe").click()
driver.find_element(By.CLASS_NAME,"buttons").click()

input("Please solve the CAPTCHA manually, then press Enter to continue...")

act_t = driver.title
exp_t = "Dashboard / nopCommerce administration"
if act_t==exp_t:
    print("Test Passed")
else:
    print("Test failed")

input("Press Enter to exit and close the browser...")
driver.quit()

