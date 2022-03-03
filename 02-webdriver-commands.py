import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.get("https://courses.ultimateqa.com/users/sign_in")

print("The title of the webpage is: " + driver.title)
print("The url of the webpage is: " + driver.current_url)
driver.find_element_by_xpath("/html/body/main/div/div/aside/a").click()
time.sleep(5)

driver.close()