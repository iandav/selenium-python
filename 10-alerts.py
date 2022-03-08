import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
time.sleep(5)
Alert(driver).accept()


