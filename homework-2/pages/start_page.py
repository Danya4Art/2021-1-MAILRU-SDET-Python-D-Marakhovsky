from locators.start_page_locators import StartPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
import allure


class StartPage(BasePage):

    locators = StartPageLocators()

    @allure.step('Login')
    def login(self, log, psw):
        self.logger.info(f'''
            login: {log}
            password: {psw}
            ''')
        self.click(self.locators.BUTTON_LOCATOR)
        self.enter(self.locators.EMAIL_LOCATOR, log)
        self.enter(self.locators.PASSWORD_LOCATOR, psw)
        self.click(self.locators.ENTER_LOCATOR)
        return MainPage(self.driver)