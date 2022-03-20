import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")

# Capture all the cookies created by the browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

# Adding a new cookie
cookie = {'name': 'myCookie', 'value':'123'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))

# Deleting a cookie
driver.delete_cookie('myCookie')
cookies = driver.get_cookies()
print(len(cookies))


driver.quit()