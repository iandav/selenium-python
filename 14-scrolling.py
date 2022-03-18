import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/")

# Scroll by pixel
driver.execute_script('window.scrollBy(0,400)','')

# Scroll until element is found
element = driver.find_element(By.CSS_SELECTOR,'a[href="/inputs"]')
driver.execute_script("arguments[0].scrollIntoView();", element)

# Scroll to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")