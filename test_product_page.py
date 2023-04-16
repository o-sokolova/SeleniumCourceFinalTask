import time
import pytest
from .pages.links import Links
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
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
        page.should_not_be_success_alert()

    @pytest.mark.need_review
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
    page.should_not_be_success_alert()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_alert()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.should_not_be_success_alert()


@pytest.mark.need_review
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Links.MAIN_PAGE)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Links.FIRST_BOOK_PAGE)
    page.open()
    page.click_button(*BasePageLocators.BUTTON_TO_BASKET)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
