import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/automation-practice-form")

# Radio buttons
maleRadioButton = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
print("Male radio button is selected:", driver.find_element_by_id("gender-radio-1").is_selected())
maleRadioButton.click()
print("Male radio button is selected:", driver.find_element_by_id("gender-radio-1").is_selected())

driver.quit()