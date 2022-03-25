import unittest
from selenium import webdriver

# Define test cases, always starting with 'test' keyword
class SearchEngines(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Majestic\Documents\QA\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_google(self):
        self.driver.get("https://google.com/")
        print(self.driver.title)
        pageTitle = self.driver.title
        # AssertEqual
        self.assertEqual(pageTitle,"Google","Title isn't the same")

    def test_duckduckgo(self):
        self.driver.get("https://duckduckgo.com/")
        print(self.driver.title)

# Execute tests
if __name__ == '__main__':
    unittest.main()