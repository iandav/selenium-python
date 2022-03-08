import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\Testing\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/redirector")

# Get all links of the webpage
links = driver.find_elements(By.TAG_NAME, "a")

# Total number of links
print("Total number of links:", len(links))

# List all links
for link in links:
    print(link.text)

# Click on links
driver.find_element_by_link_text("here").click()


driver.quit()





