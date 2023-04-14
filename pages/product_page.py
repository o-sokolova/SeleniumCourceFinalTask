import math
from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()

    def check_add(self):
        result = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT)
        text = result.text
        expected_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert expected_name in text, f"'{expected_name}' should be contained in '{text}'"

    def check_sum(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert product_price == basket_price, f"product_price={product_price} != basket_price={basket_price}"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
