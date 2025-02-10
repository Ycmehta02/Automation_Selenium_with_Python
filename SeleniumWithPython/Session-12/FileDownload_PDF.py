##PDF File ----------------------------------------------------------------------------------

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    pref = {"download.default_directory": location, "plugins.always_open_pdf_externally":True} #save files in desired location #dictionary
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("prefs", pref) #desired location
    driver = webdriver.Chrome(service=serv, options=opt)
    # driver = webdriver.Chrome(service=serv)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    pref = {"download.default_directory": location, "plugins.always_open_pdf_externally":True} #save files in desired location #dictionary
    opt = webdriver.EdgeOptions()
    opt.add_experimental_option("prefs", pref) #desired location
    driver = webdriver.Edge(service=serv, options=opt)
    # driver = webdriver.Chrome(service=serv)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv = Service(r"C:\Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
    #settings
    opt = webdriver.FirefoxOptions()

    ### mime type
    # https://www.sitepoint.com/mime-types-complete-list/#h-key-takeaways
    # opt.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    opt.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    opt.set_preference("browser.download.manager.showWhenStarting", False)
    opt.set_preference("browser.download.folderList",2)
    # 0 -> desktop,  1 --> default location, 2 --> desired location
    opt.set_preference("pdfjs.disabled",True) #for pdf
    opt.set_preference("browser.download.dir",location)

    driver = webdriver.Firefox(service=serv, options=opt)
    return driver

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")

driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)
