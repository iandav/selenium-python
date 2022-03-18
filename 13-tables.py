import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/tables")


# Count total rows (using xpath)
tableRows = len(driver.find_elements(By.XPATH,"/html/body/div[2]/div/div/table[1]/tbody/tr"))
print('Number of rows:', tableRows)

# Count total columns (using xpath)
tableColumns = len(driver.find_elements(By.XPATH,"/html/body/div[2]/div/div/table[1]/thead/tr/th"))
print('Number of columns:', tableColumns)

# Read tables
for r in range(tableRows+1):
    for c in range(tableColumns+1):
        value = driver.find_element_by_xpath("/html/body/div[2]/div/div/table[1]/tbody/tr["+str(r)+"]/td["+str(c)+"]")
        print(value.text)

driver.quit()

# For some reaseon the above exercice doesn't work...
