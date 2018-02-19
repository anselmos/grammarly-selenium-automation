
from bs4 import BeautifulSoup

class DocumentScraper(object):

    def __init__(self, html_source):
        # self.html_source = html_source
        self.bs = BeautifulSoup(html_source, "html.parser")

    def get_issue_div(self):
        # DIV with class=_adbfa1e6-editor-page-cardsCol
        return self.bs.find('div', {'class': '_adbfa1e6-editor-page-cardsCol'})

    def get_all_warnings(self):
        return self.get_issue_div().contents

    def get_all_warnings_texts(self):
        return [element.text for element in  self.get_all_warnings()]

    def iterate_over_warnings(self):
        for innerelement in self.get_all_warnings():
            print innerelement.text
