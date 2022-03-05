import time
from xml.etree.ElementTree import tostring
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.get("https://courses.ultimateqa.com/users/sign_in")
time.sleep(3)
emailField = driver.find_element_by_id("user[email]")

print("The element is displayed: " + str(emailField.is_displayed()))
print("The element field is enabled: " + str(emailField.is_enabled()))

driver.quit()

