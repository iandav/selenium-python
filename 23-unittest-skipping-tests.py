import unittest
import time
from selenium import webdriver

# Define test cases, always starting with 'test' keyword
class SearchEngines(unittest.TestCase):

    @unittest.SkipTest
    def test_google(self):
        print("Google")
    
    @unittest.skip("Skip this test for now")
    def test_duckduckgo(self):
        print("Duckduckgo")

    @unittest.skipIf(False, "FALSE, this test will be executed")
    def test_bing(self):
        print("Bing")
    
    def test_yahoo(self):
        print("Yahoo")

# Execute tests
if __name__ == '__main__':
    unittest.main()