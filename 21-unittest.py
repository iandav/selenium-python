import unittest
from selenium import webdriver

# Define test cases, always starting with 'test' keyword
class SearchEngines(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://google.com/")

        print(self.driver.title)
        self.driver.quit()

    def test_duckduckgo(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://duckduckgo.com/")

        print(self.driver.title)
        self.driver.quit()

# Execute tests
if __name__ == '__main__':
    unittest.main()