import time
import pytest
from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login
from pages.settings import url_profile_page


@pytest.mark.smoke
def test_go_to_logo_button(browser):
    test_go_to_login(browser)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo_button()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/back_to_main_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_quit_button(browser):
    test_go_to_login(browser)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_quit_button()
    time.sleep(7)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/quit.png')


@pytest.mark.smoke
def test_go_to_add_pet(browser):
    test_go_to_login(browser)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_button()
    page.go_to_add_pet_name()
    page.go_to_add_pet_age()
    page.go_to_choose_pet_type()
    page.go_to_choose_pet_type_cat()
    page.go_to_choose_pet_gender()
    page.go_to_choose_pet_gender_male()
    page.go_to_submit_add_pet_button()
    page.open()
    time.sleep(7)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/new_pet.png')


@pytest.mark.smoke
def test_delete_pet(browser):
    test_go_to_login(browser)
    link = url_profile_page
    page = ProfilePage(browser, link)
    page.open()
    page.delete_pet_d()
    time.sleep(5)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/delete_new_pet.png')
