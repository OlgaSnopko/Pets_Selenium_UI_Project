from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_LOGIN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a')
    MAIN_REGISTER = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    MAIN_FILTER_BY_TYPE = (By.ID, 'typesSelector')
    MAIN_FILTER_BY_HUMSTER = (By.ID, 'pv_id_2_3')
    FILTER_BY_PET_NAME = (By.ID, 'petName')
    NEXT_PAGE = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[3]/button[3]')
    PET_DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div/div/div[3]/div[1]/button')
    PETS_ICON = (By.CSS_SELECTOR, "#app > header > div > div")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")
    LOGIN_IMAGE = (By.CSS_SELECTOR, "#app > header > div > div")
    LOGIN_REGISTRATION = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a')


class ProfilePageLocators:
    LOGO_BTN = (By.CLASS_NAME, 'p-menubar-start')
    QUIT_BTN = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(2) > a')
    ADD_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    ADD_PET_NAME = (By.ID, 'name')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_CAT = (By.XPATH, "//li[@id='pv_id_2_1']")
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    SUBMIT_ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    DELETE_PET_D = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[4]/div/div[2]/button[2]')
    DELETE_PET_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
