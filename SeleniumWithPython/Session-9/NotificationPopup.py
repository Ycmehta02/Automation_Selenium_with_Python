#for location or other access notification browser popups
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications") #setting browser level argument
serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv,option = op)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
