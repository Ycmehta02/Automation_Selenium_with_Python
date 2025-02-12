import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import XLUtils

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

# driver.switch_to.alert.dismiss()
alert = driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']")
alert.click()
time.sleep(5)

file =r"C:\Users\Alian\Desktop\YM\calcdata.xlsx"

rows = XLUtils.getRowCount(file,"Sheet1")

p_s = driver.find_element(By.XPATH, "//input[@id='principal']")
r_s = driver.find_element(By.XPATH, "//input[@id='interest']")
pe_s = driver.find_element(By.XPATH, "//input[@id='tenure']")
pe_day_s = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
f_s = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
cal_btn = driver.find_element(By.XPATH, "//div[@class='cal_div']//a[1]")
act_val = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
clear = driver.find_element(By.XPATH, "//div[@class='MT10']//a[2]")

for r in range(2,rows+1):
    p = XLUtils.readData(file,"Sheet1", r,1)
    rate = XLUtils.readData(file,"Sheet1",r,2)
    p1 = XLUtils.readData(file, "Sheet1",r, 3)
    p2 = XLUtils.readData(file, "Sheet1", r, 4)
    f = XLUtils.readData(file, "Sheet1", r, 5)
    exp_mv = XLUtils.readData(file, "Sheet1", r, 6)

    #passing data to the application
    p_s.send_keys(p) #principle field
    r_s.send_keys(rate) #Rate of interest field
    pe_s.send_keys(p1) #Period no
    pe_day_s.select_by_visible_text(p2) #Period option Ex. day, year, month
    f_s.select_by_visible_text(f)
    cal_btn.click() #Calculate button
    act_val = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
    time.sleep(5)

    #Validation
    if float(exp_mv)==float(act_val):
        print("Test Passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    clear.click()
    time.sleep(5)

driver.quit()
