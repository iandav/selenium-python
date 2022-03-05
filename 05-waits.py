import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")

# Implicit wait
#driver.get("https://www.saucedemo.com/")
#driver.implicitly_wait(10)

#assert "Swag Labs" in driver.title

#driver.find_element_by_id("user-name").send_keys("standard_user")
#driver.find_element_by_id("password").send_keys("secret_sauce")
#driver.find_element_by_id("login-button").click()

# Explicit wait
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)

assert "Swag Labs" in driver.title

driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")

# The following code will wait max 10 seconds until the login button is clickable
# When the condition is TRUE, the element will be stored in a variable and all the following actions will be performed
element = wait.until(EC.element_to_be_clickable(driver.find_element_by_id("login-button")))
element.click()

time.sleep(10)
driver.quit()