from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.fill_field(*LoginPageLocators.REGISTER_EMAIL, email)
        self.fill_field(*LoginPageLocators.REGISTER_PSW, password)
        self.fill_field(*LoginPageLocators.REGISTER_REPEATED_PSW, password)
        self.click_button(*LoginPageLocators.REGISTER_BTN)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        print(current_url)
        assert "login" in current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
