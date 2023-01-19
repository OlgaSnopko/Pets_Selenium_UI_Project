import pytest
import time
from pages.main_page import MainPage
from pages.settings import url_main_page


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_login_page(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/login_page_after_main_page.png')


@pytest.mark.smoke
@pytest.mark.regression
def test_go_to_registration_page(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_registration_page()
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/registration_page_after_main_page.png')


@pytest.mark.regression
def test_go_to_filter_by_humster(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    page.go_to_filter_by_humster()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/all_hamsters.png')


@pytest.mark.regression
def test_go_to_filter_by_pet_name(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/filter_by_pet_name_Atos.png')


@pytest.mark.smoke()
@pytest.mark.regression()
def test_go_to_pet_details(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    page.go_to_pet_details()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/Atos_page.png')


@pytest.mark.skip
def test_go_to_next_page(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_next_page()
    time.sleep(2)
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/next_page_after_main_page.png')


@pytest.mark.xfail
def test_go_to_image(browser):
    link = url_main_page
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page_icon()
    browser.save_screenshot('Pets_Selenium_UI_Project/tests/return_from_Atos.png')
