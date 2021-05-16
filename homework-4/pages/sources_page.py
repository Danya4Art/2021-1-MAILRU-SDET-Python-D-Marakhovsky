from locators import SourcesPageLocators
from pages.base_page import BasePage    
import allure    


class SourcesPage(BasePage):

    locators = SourcesPageLocators()

    @allure.step('Change source to Vesti FM')
    def select_vesti(self):
        self.logger.info('Change source to vesti FM') 
        self.click(self.locators.VESTI_FM_LOCATOR)
        self.find(self.locators.SELECTED_LOCATOR)
        self.click(self.locators.BACK_LOCATOR)