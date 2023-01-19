from .base_page import BasePage
from .locators import ProfilePageLocators
from pages.settings import dartaniyan
from pages.settings import age


class ProfilePage(BasePage):
    def go_to_logo_button(self):
        logo_button = self.browser.find_element(*ProfilePageLocators.LOGO_BTN)
        logo_button.click()

    def go_to_quit_button(self):
        quit_button = self.browser.find_element(*ProfilePageLocators.QUIT_BTN)
        quit_button.click()

    def go_to_add_pet_button(self):
        add_pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BTN)
        add_pet_button.click()

    def go_to_add_pet_name(self):
        add_pet_name = self.browser.find_element(*ProfilePageLocators.ADD_PET_NAME)
        add_pet_name.send_keys(dartaniyan)

    def go_to_add_pet_age(self):
        add_pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        add_pet_age.send_keys(age)

    def go_to_choose_pet_type(self):
        choose_pet_type = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE)
        choose_pet_type.click()

    def go_to_choose_pet_type_cat(self):
        choose_pet_type_cat = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE_CAT)
        choose_pet_type_cat.click()

    def go_to_choose_pet_gender(self):
        choose_pet_gender = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER)
        choose_pet_gender.click()

    def go_to_choose_pet_gender_male(self):
        choose_pet_gender_male = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER_MALE)
        choose_pet_gender_male.click()

    def go_to_submit_add_pet_button(self):
        submit_add_pet_button = self.browser.find_element(*ProfilePageLocators.SUBMIT_ADD_PET_BTN)
        submit_add_pet_button.click()

    def delete_pet_d(self):
        delete_new_pet = self.browser.find_element(*ProfilePageLocators.DELETE_PET_D)
        delete_new_pet.click()
        yes_delete = self.browser.find_element(*ProfilePageLocators.DELETE_PET_YES)
        yes_delete.click()
