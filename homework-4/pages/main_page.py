from selenium.webdriver.common.by import By
from locators import MainPageLocators
from pages.base_page import BasePage
from pages.settings_page import SettingsPage
import allure


class MainPage(BasePage):

    locators = MainPageLocators()

    @allure.step('Search Russia')
    def search_russia(self):
        self.logger.info('Search Russia') 
        self.click(self.locators.KEYBOARD_BUTTON)
        self.enter(self.locators.SEARCH_LINE, "Russia")
        self.click(self.locators.INPUT_BUTTON)
        self.logger.debug('Hide keyboard')
        self.driver.hide_keyboard()
        assert "России" in self.find(self.locators.CARD_LOCATOR).get_attribute('text')
        next_message = (By.XPATH, self.locators.ANSWER_LOCATOR.format('население россии'))
        swipe_elem = self.find(self.locators.ANSWER_LIST_LOCATOR)
        self.swipe_to_element(next_message, position='right', swipe_elem=swipe_elem)
        self.click(next_message)
        self.find((By.XPATH, self.locators.ANSWER_LOCATOR.format('146 млн.')))

    @allure.step('Check search Vesti FM')
    def check_vesti(self):
        self.click(self.locators.KEYBOARD_BUTTON)
        self.enter(self.locators.SEARCH_LINE, "News")
        self.click(self.locators.INPUT_BUTTON)
        self.logger.debug('Hide keyboard')
        self.driver.hide_keyboard()
        self.logger.info('Check Vesti FM is selected') 
        self.find((By.XPATH, self.locators.ANSWER_LOCATOR.format('Включаю новости Вести FM.')))

    @allure.step('Calculate {expression}')
    def calculate(self, expression):
        self.click(self.locators.KEYBOARD_BUTTON)
        self.logger.debug('Input expression') 
        self.enter(self.locators.SEARCH_LINE, expression)
        self.click(self.locators.INPUT_BUTTON)
        result = int(self.find(self.locators.RESULT_LOCATOR).get_attribute('text'))
        self.logger.info(f'Return result {result}') 
        return result
    
    @allure.step('Open settings')
    def open_settings(self):
        self.logger.debug('Open settings') 
        self.click(self.locators.BURGER_MENU)
        return SettingsPage(self.driver)