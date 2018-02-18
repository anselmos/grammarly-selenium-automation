import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://github.com")
        assert "GitHub" in driver.title
        elem = driver.find_element_by_name("q")
        elem.send_keys("anselmos")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
