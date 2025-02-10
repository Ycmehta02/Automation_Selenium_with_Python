from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

min_slider = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
max_slider = driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]//*[@id='slider-range']/span[2]")

print("Before Moving:")
print(min_slider.location)
print(max_slider.location)

#Drag Slider

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()

act.drag_and_drop_by_offset(max_slider,-40,0).perform()

print("After Moving")
print(min_slider.location)
print(max_slider.location)


