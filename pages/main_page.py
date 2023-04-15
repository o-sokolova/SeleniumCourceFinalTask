from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, browser, url, *args, **kwargs):
        super().__init__(browser, url)