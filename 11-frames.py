import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame(1)
driver.switch_to.default_content()

driver.quit()

