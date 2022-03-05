import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.get("https://courses.ultimateqa.com/users/sign_in")
time.sleep(3)