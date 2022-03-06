import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Firefox driver
driver = webdriver.Firefox(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\geckodriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")

# Find total number of input elements present in the webpage
inputBoxes = driver.find_elements(By.CLASS_NAME, "form_group")
print(len(inputBoxes))

# Add text value
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")

# Check stauts of the input boxes
print("Input box is enabled: ", driver.find_element_by_id("user-name").is_enabled())
print("Input box is displayed: ", driver.find_element_by_id("user-name").is_displayed())

driver.quit()
