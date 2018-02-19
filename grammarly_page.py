from page_objects import PageObject, PageElement
import time


class GrammarlyLogin(PageObject):
    username = PageElement(css='input[type="email"]')
    password = PageElement(css='input[type="password"]')
    login = PageElement(css='button[type="submit"]')
    uri = 'https://www.grammarly.com'
    signin_uri = '/signin'

    def make_login(self, username, password):
        self.get(self.uri + self.signin_uri)
        self.username = username
        self.password = password
        self.login.click()
        #TODO replace this with Wait.Untill selenium feature.
        time.sleep(2)


class GrammarlyNewDocument(PageObject):
    uri = 'https://app.grammarly.com/'
    new_document = PageElement(css='div[role="button"]')

    def make_new_document(self, name=None):
        self.get(self.uri)
        self.new_document.click()
        time.sleep(2)


class GrammarlyDocument(PageObject):

    title = PageElement(css='input[type="text"]')
    text = PageElement(id_='textarea')
    # This button below will only be visible for grammarly premium users.
    score_button = PageElement(css='span[class="_ff9902-score"]')
    download_pdf_btn = PageElement(css='div[class="_d0e45e-button _d0e45e-medium"]')

    def put_title(self, title):
        self.title = title

    def put_text(self, text):
        self.text = text
        time.sleep(10)

    def get_page_source(self):
        return self.w.page_source