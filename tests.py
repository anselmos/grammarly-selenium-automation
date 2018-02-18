import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from grammarly_page import GrammarlyLogin
from grammarly_page import GrammarlyNewDocument
import time

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
        page_login = GrammarlyLogin(self.driver)
        self.driver.get(page_login.uri)
        assert "Grammarly" in self.driver.title

    def test_login(self):
        page_login = GrammarlyLogin(self.driver)
        page_login.make_login('za2217279@mvrht.net', 'test123')
        assert self.driver.current_url == "https://app.grammarly.com/"

    def test_make_new_doc(self):
        page_login = GrammarlyLogin(self.driver)
        page_login.make_login('za2217279@mvrht.net', 'test123')
        page_new_doc = GrammarlyNewDocument(self.driver)
        page_new_doc.make_new_document("TEST")
        assert "https://app.grammarly.com/docs/" in self.driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
