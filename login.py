import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GrammarlyGeneralTest(unittest.TestCase):

    def setUp(self):
        # for dev I'll use only visible browser instead of no-gui one.
        # but for production, it will use the no-gui one.
        self.driver = webdriver.Firefox()
        # TODO uncomment it when finished coding.
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
        # )

    def test_grammarly_in_title(self):
        driver = self.driver
        driver.get("https://grammarly.com")
        assert "Grammarly" in driver.title

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
