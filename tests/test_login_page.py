import pytest
import time
from pages.login_page import LoginPage
from pages.settings import url_login_page


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_login(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_login_button()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/my_pets_after_login_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_image(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_image()
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/all_pets_after_login_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_registration_button(browser):
    link = url_login_page
    page = LoginPage(browser, link)
    page.open()
    page.go_to_registration_button()
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/page_registration_after_login_page.png')
