import time
import pytest
from .pages.links import Links
from pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        psw = str(time.time()) + "qwe)(*&"
        login_page = LoginPage(browser, Links.LOGIN_PAGE)
        login_page.open()
        login_page.register_new_user(email, psw)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "Alert is present although it shouldn't"

    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
        page.open()
        page.add_to_basket()
        page.check_add()
        page.check_sum()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "Alert is present although it shouldn't"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_ALERT), "Alert is not disappeared although it should"


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_ALERT), "Alert is present although it shouldn't"


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                       "/?promo=offer7", marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_add()
    page.check_sum()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Links.SECOND_BOOK_PAGE)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = ProductPage(browser, Links.MAIN_PAGE)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.click_button(*BasePageLocators.BUTTON_TO_BASKET)
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.is_basket_empty(), "Basket must be empty"
    assert basket_page.is_empty_basket_text_present(), "Empty basket text doesn't present"
