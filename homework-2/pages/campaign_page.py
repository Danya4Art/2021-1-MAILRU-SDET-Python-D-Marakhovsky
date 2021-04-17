from locators.campaign_page_locators import CampaignPageLocators
from pages.main_page import BasePage    
import allure    


class CampaignPage(BasePage):

    locators = CampaignPageLocators()

    @allure.step('Create campaign')
    def create_campaign(self, link, image):
        self.logger.info(f'''
            Creating new campaign with
            URL: {link}
            ''')
        self.logger.debug('Choose traffic type')
        self.click(self.locators.TRAFFIC_LOCATOR)
        self.logger.debug('Paste link')
        self.enter(self.locators.LINK_LOCATOR, link)
        name = self.find(self.locators.NAME_LOCATOR).get_attribute('value')
        self.logger.debug('Scroll to banner')
        self.action_chains.move_to_element(self.find(self.locators.BANNER_LOCATOR)).click().perform()
        self.logger.debug('Scroll to picture place')
        self.action_chains.move_to_element(self.find(self.locators.IMAGE_LOCATOR)).perform()
        self.enter(self.locators.INPUT_LOCATOR, image)
        self.click(self.locators.CREATE_LOCATOR)
        self.logger.info(f'''
            New campaign created with name:
            {name}
            ''')
        return name