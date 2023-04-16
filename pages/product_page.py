import math
from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_button(*ProductPageLocators.ADD_TO_BASKET)

    def check_add(self):
        result = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT)
        text = result.text
        expected_text = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert expected_text == text, f"Expected alert = '{expected_text}'\n" \
                                      f"Fact alert = '{text}'"

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

    def should_not_be_success_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "Alert is present although it shouldn't"

    def should_be_disappeared_alert(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Alert is not disappeared although it should"
