import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

#SQL Connection----------------------------------------------
import mysql.connector

# insert_q = "insert into student values(104,'XYZ')"
# update_q = "update student set sname='Mary' where sid=104;"
# delete_q = "delete from student where sid=104"
select_q = "select * from caldata"

#---------------------------------------------------------

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

#SQL Operations----------------------------------------------------
# con = mysql.connector.connect(host="localhost", port=3306, user="root", password="root", database="mydb")
# cur = con.cursor()  # thorugh cursor the operations will be performed on DB
# cur.execute(insert_q)  # query execution with cursor
# cur.execute(update_q)
# cur.execute(delete_q)
# cur.execute(select_q)
# con.commit()  # commit transaction
# con.close()

#-----------------------------------------------------------------

# driver.switch_to.alert.dismiss()
alert = driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']")
alert.click()
time.sleep(5)



p_s = driver.find_element(By.XPATH, "//input[@id='principal']")
r_s = driver.find_element(By.XPATH, "//input[@id='interest']")
pe_s = driver.find_element(By.XPATH, "//input[@id='tenure']")
pe_day_s = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
f_s = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
cal_btn = driver.find_element(By.XPATH, "//div[@class='cal_div']//a[1]")
act_val = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text
clear = driver.find_element(By.XPATH, "//div[@class='MT10']//a[2]")


try:

    con = mysql.connector.connect(host="localhost",user="root", password="root", port=3306, database="mydb")
    cur = con.cursor()
    cur.execute(select_q)

    for r in cur:
        p =r[0]
        rate =r[1]
        p1 =r[2]
        p2 =r[3]
        f =r[4]
        exp_mv =r[5]

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

        else:
            print("Test Failed")

        clear.click()
        time.sleep(5)

except:
    print("Connection unsuccessful")


driver.quit()
# con.commit()  # commit transaction
con.close()