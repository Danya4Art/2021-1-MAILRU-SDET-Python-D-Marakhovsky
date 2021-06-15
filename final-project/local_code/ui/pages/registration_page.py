from selenium.webdriver.common.by import By
import allure
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.locators.registration_page_locators import RegistrationPageLocators

class RegistrationPage(BasePage):

    locators = RegistrationPageLocators()

    @allure.step('Login')
    def registrate(self, log, email, psw):
        self.logger.info(f'''
            login: {log}
            email: {email}
            password: {psw}
            ''')
        self.enter(self.locators.USERNAME_LOCATOR, log)
        self.enter(self.locators.EMAIL_LOCATOR, email)
        self.enter(self.locators.PASSWORD_LOCATOR, psw)
        self.enter(self.locators.CONFIRM_LOCATOR, psw)
        self.click(self.locators.TERM_LOCATOR)
        self.click(self.locators.SUBMIT_LOCATOR)
        return MainPage(self.driver)

    @allure.step('Open registration page')
    def open_login_page(self):
        self.click((By.XPATH, self.locators.CHANGE_PAGE_LOCATOR.format('login')))
    