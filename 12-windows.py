import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")

print(driver.title)
print(driver.current_window_handle)

driver.find_element(By.CSS_SELECTOR, "a[href='/windows/new']").click()
print(driver.window_handles)
time.sleep(5)
driver.switch_to.window("CDwindow-DCBB27B5F4B37CA053F169EFDB0B9889")

driver.quit()


