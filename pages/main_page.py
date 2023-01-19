from selenium.webdriver.common.keys import Keys
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        main_login = self.browser.find_element(*MainPageLocators.MAIN_LOGIN)
        main_login.click()

    def go_to_registration_page(self):
        main_register = self.browser.find_element(*MainPageLocators.MAIN_REGISTER)
        main_register.click()

    def go_to_filter_by_type(self):
        main_filter_by_type = self.browser.find_element(*MainPageLocators.MAIN_FILTER_BY_TYPE)
        main_filter_by_type.click()

    def go_to_filter_by_humster(self):
        main_filter_by_humster = self.browser.find_element(*MainPageLocators.MAIN_FILTER_BY_HUMSTER)
        main_filter_by_humster.click()

    def go_to_filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.send_keys('Atos')
        filter_by_pet_name.send_keys(Keys.RETURN)

    def go_to_next_page(self):
        next_page = self.browser.find_element(*MainPageLocators.NEXT_PAGE)
        next_page.click()

    def go_to_pet_details(self):
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS)
        pet_details.click()

    def go_to_login_page_icon(self):
        return_from_filter_page = self.browser.find_element(*MainPageLocators.PETS_ICON)
        return_from_filter_page.click()
