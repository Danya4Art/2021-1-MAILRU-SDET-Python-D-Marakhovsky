from selenium.webdriver.common.by import By
from ui.locators.login_page_locators import LoginPageLocators

class RegistrationPageLocators(LoginPageLocators):

    EMAIL_LOCATOR = (By.ID, 'email')
    CONFIRM_LOCATOR = (By.ID, 'confirm')
    TERM_LOCATOR = (By.ID, 'term')
    