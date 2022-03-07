import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dropdown")

# Select an option
dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_value("1")

# Total number of options
print(len(dropdown.options))

# List all options
dropdown_options = dropdown.options
for i in dropdown_options:
    print(i.text)

driver.quit()






