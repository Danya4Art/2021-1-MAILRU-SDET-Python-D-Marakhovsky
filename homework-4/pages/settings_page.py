from locators import SettingsPageLocators        
from pages.base_page import BasePage
from pages.sources_page import SourcesPage
from pages.info_page import InfoPage
import allure


class SettingsPage(BasePage):

    locators = SettingsPageLocators()

    @allure.step('Open sources')
    def open_sources(self):
        self.logger.info('') 
        self.swipe_to_element(self.locators.NEWS_SOURCES)
        self.click(self.locators.NEWS_SOURCES)
        return SourcesPage(self.driver)

    @allure.step('Open info')
    def open_info(self):
        self.logger.info('') 
        self.swipe_to_element(self.locators.ABOUT_LOCATOR)
        self.click(self.locators.ABOUT_LOCATOR)
        return InfoPage(self.driver)

    def back_to_main_page(self):
        self.logger.info('') 
        self.click(self.locators.EXIT_LOCATOR)