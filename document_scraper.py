
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

    def find_all_issues(self):
        return self.bs.findAll('div', {'class': '_ed4374-title'})

    def return_issues_by_type(self):
        issues = self.find_all_issues()
        output = {}
        for issue in issues:
            key = issue.contents[0].attrs['class'][0]
            try:
                output[key].append(issue.contents[0].contents)
            except KeyError:
                output[key] = [issue.contents[0].contents]

        return output

