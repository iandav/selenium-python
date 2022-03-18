import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Chrome driver
driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/hovers")

# Mouse Hover
user1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/img')
user3 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/img')

actions = ActionChains(driver).move_to_element(user1).move_to_element(user3)
actions.perform()

time.sleep(5)

# Double click
driver.get('https://mousetester.com/')
button = driver.find_element(By.ID,'clickMe')

actions2 = ActionChains(driver).double_click(button)
actions2.perform()

time.sleep(5)

# Right click
driver.get('https://mousetester.com/')
button = driver.find_element(By.ID,'clickMe')

actions2 = ActionChains(driver).context_click(button)
#actions2.perform()

time.sleep(5)

# Drag and drop
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
sourceElement = driver.find_element(By.XPATH,'//*[@id="column-a"]')
targetElement = driver.find_element(By.XPATH,'//*[@id="column-b"]')

dragDrop = ActionChains(driver).drag_and_drop(sourceElement,targetElement)
dragDrop.perform()

time.sleep(5)