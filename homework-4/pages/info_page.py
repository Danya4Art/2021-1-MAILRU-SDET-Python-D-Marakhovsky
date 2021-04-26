from locators import InfoPageLocators
from pages.base_page import BasePage
from capabilities import DESIRED_CAPS
import allure
import re


class InfoPage(BasePage):

    locators = InfoPageLocators()

    @allure.step('Check info')
    def check_info(self):
        self.logger.info('Check info') 
        apk_version = re.findall(r'v(.+).apk', DESIRED_CAPS['app'])
        self.logger.debug('Check version') 
        assert apk_version[0] in self.find(self.locators.VERSION_LOCATOR).get_attribute('text')
        self.logger.debug('Check rights')
        assert 'Все права защищены' in self.find(self.locators.ALL_RIGHTS_RESERVED_LOCATOR).get_attribute('text')