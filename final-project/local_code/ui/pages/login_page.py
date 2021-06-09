from selenium.webdriver.common.by import By
import allure
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.registration_page import RegistrationPage
from ui.locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

    locators = LoginPageLocators()

    @allure.step('Login')
    def login(self, log, psw):
        self.logger.info(f'''
            login: {log}
            password: {psw}
            ''')
        self.enter(self.locators.USERNAME_LOCATOR, log)
        self.enter(self.locators.PASSWORD_LOCATOR, psw)
        self.click(self.locators.SUBMIT_LOCATOR)
        return MainPage(self.driver)

    @allure.step('Open registration page')
    def open_registration_page(self):
        self.click((By.XPATH, self.locators.CHANGE_PAGE_LOCATOR.format('reg')))
        return RegistrationPage(self.driver)