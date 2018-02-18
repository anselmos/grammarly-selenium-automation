from page_objects import PageObject, PageElement
from selenium import webdriver

class GrammarlyLogin(PageObject):
    username = PageElement(id_='input[type="email"]')
    password = PageElement(css='input[type="password"]')
    login = PageElement(css='input[type="submit"]')

    def make_login(self, username, password):
        self.username = username
        self.password = password
        self.login.click()

