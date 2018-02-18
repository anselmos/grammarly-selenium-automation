from page_objects import PageObject, PageElement

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


