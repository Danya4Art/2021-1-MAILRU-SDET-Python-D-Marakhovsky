from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.campaign_page import CampaignPage
from pages.segments_page import SegmentsPage
import allure


class MainPage(BasePage):

    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.pages = {
                'SEGMENTS': SegmentsPage, 
                'CAMPAIGN': CampaignPage
                }

    @allure.step('Logout')
    def logout(self):
        self.logger.debug('Logout')
        self.click(self.locators.RIGHT_MODULE_LOCATOR)
        self.click(self.locators.BUTTONS_LOCATORS['LOGOUT'])
        return StartPage(self.driver)

    @allure.step('Open {new_page} page')
    def open_page(self, new_page):
        self.logger.debug(f'Open {new_page} page')
        self.click(self.locators.BUTTONS_LOCATORS[new_page])
        if new_page in self.pages.keys():
            return self.pages[new_page](self.driver)

    @allure.step('Delete campaign {name}')
    def delete_campaign(self, name, every=False):
        self.logger.info('Campaign deletion')
        if every:
            self.logger.debug('Delete all campaigns')
            self.click(self.locators.MARK_ALL_LOCATOR)
        else:
            self.logger.debug(f'Delete {name} campaign')
            campaign_mark = self.locators.MARK_CAMPAIGN_LOCATOR(name)
            self.click(campaign_mark)
        self.click(self.locators.ACTIONS_LOCATOR)
        self.click(self.locators.DELETE_LOCATOR)

    @allure.step('Check campaign {name}')
    def check_campaign(self, name):
        try:
            self.find(self.locators.MARK_CAMPAIGN_LOCATOR(name), find_wait=10)
            self.logger.debug('Campaign exist')
            return True
        except:
            self.logger.debug('Campaign doesn\'t exist')
            return False