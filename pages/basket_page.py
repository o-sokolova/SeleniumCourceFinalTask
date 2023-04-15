from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)

    def is_empty_basket_text_present(self):
        return self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT)
