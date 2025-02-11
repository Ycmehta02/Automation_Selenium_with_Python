import time

from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    ops =webdriver.ChromeOptions()
    # ops.headless=True
    ops.add_argument("--headless=new")  # Correct way to enable headless mode
    driver = webdriver.Chrome(service=serv,options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    ops =webdriver.EdgeOptions()
    # ops.headless=True
    ops.add_argument("--headless=new")  # Correct way to enable headless mode
    driver = webdriver.Edge(service=serv,options=ops)
    return driver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv = Service(r"C:\Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
    ops =webdriver.FirefoxOptions()
    # ops.headless=True
    ops.add_argument("--headless=new")  # Correct way to enable headless mode
    driver = webdriver.Firefox(service=serv,options=ops)
    return driver

# driver = headless_chrome()
# driver = headless_edge()
driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/")
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.quit()