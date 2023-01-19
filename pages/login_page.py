from .base_page import BasePage
from .locators import LoginPageLocators
from .settings import login
from .settings import password


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys(login)

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)

    def go_to_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()

    def go_to_image(self):
        login_image = self.browser.find_element(*LoginPageLocators.LOGIN_IMAGE)
        login_image.click()

    def go_to_registration_button(self):
        login_registration = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION)
        login_registration.click()
