# -*- coding: utf-8 -*-
import unittest
from document_scraper import DocumentScraper
from grammarly_page import GrammarlyLogin
from grammarly_page import GrammarlyNewDocument
from grammarly_page import GrammarlyDocument
import time


class GrammarlyScrapingTests(unittest.TestCase):


    def test1(self):
        filename = "bs_output_test1.html"
        with open(filename, 'r+') as f:
            self.data_scrape1 = f.read()

        assert len(self.data_scrape1) == 21022
        scraper = DocumentScraper(self.data_scrape1)
        expected = [("Incorrect spacingwraps             after → wraps after".decode("utf-8"))]
        result = list(scraper.get_all_warnings_texts())
        assert result == expected

    def tests_all_in_one(self):
        from selenium import webdriver
        self.driver = webdriver.Firefox()
        filename = "demo_document.txt"
        demo_data_text = None
        with open(filename, 'r+') as f:
            demo_data_text = f.read().decode("utf-8")
        page_login = GrammarlyLogin(self.driver)
        page_login.make_login('za2217279@mvrht.net', 'test123')
        page_new_doc = GrammarlyNewDocument(self.driver)
        page_new_doc.make_new_document("")
        page_doc = GrammarlyDocument(self.driver)
        page_doc.put_title("DEMO DATA TEXT")
        page_doc.put_text(demo_data_text)
        page_source = GrammarlyDocument(self.driver)
        actual_source = page_source.get_page_source()
        scraper = DocumentScraper(actual_source)
        found_issues = scraper.find_all_issues()
        assert len(found_issues) == 14
        issues_by_type = scraper.return_issues_by_type()
        assert len(issues_by_type) == 2
        assert u'_ed4374-plainTextTitle' in issues_by_type
        assert u'_ed4374-titleReplacement' in issues_by_type
        assert len(issues_by_type['_ed4374-plainTextTitle']) == 3
        assert len(issues_by_type['_ed4374-titleReplacement']) == 11
        self.driver.maximize_window()
        # making a screenshot!:
        self.driver.save_screenshot('grammarly_checks.png')
        self.driver.get_screenshot_as_file('grammarly_checks2.png')

    def tearDown(self):
        try: self.driver.close()
        except: pass

if __name__ == "__main__":
    unittest.main()