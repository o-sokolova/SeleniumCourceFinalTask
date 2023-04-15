from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_TO_BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(3) .alertinner p strong")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".content #content_inner p")
