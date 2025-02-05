
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service= serv)

# wait = WebDriverWait(driver,10) #explicit wait declaration

wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                        ElementNotVisibleException,
                                                        ElementNotSelectableException,
                                                        Exception])

#opening the application url
driver.get("https://www.google.com/")
driver.maximize_window()

ele = driver.find_element(By.NAME,'q')
ele.send_keys("Selenium")
ele.submit()

search= wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search.click()
