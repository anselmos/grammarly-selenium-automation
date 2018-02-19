# -*- coding: utf-8 -*-
import unittest
from document_scraper import DocumentScraper

class GrammarlyScrapingTests(unittest.TestCase):

    def setUp(self):

        filename = "bs_output_test1.html"
        with open(filename, 'r+') as f:
            self.data_scrape1 = f.read()


    def test1(self):
        assert len(self.data_scrape1) == 21022
        scraper = DocumentScraper(self.data_scrape1)
        expected = [("Incorrect spacingwraps             after → wraps after".decode("utf-8"))]
        result = list(scraper.get_all_warnings_texts())
        assert result == expected

if __name__ == "__main__":
    unittest.main()