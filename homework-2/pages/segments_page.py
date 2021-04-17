from locators.segments_page_locators import SegmentsPageLocators        
from pages.main_page import BasePage
import allure


class SegmentsPage(BasePage):

    locators = SegmentsPageLocators()

    @allure.step('Create segment')
    def create_segment(self):
        self.logger.info('Segment creation')
        try:
            self.click(self.locators.NEW_SEGMENT_LOCATOR[0])
        except:
            self.click(self.locators.NEW_SEGMENT_LOCATOR[1])
        self.logger.debug('Segment settings')
        self.click(self.locators.APPS_LOCATOR)
        self.click(self.locators.PLAY_PAY_LOCATOR)
        self.click(self.locators.MARK_PAY_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_LOCATOR)
        self.logger.debug('Get segment name')
        name = self.find(self.locators.NAME_LOCATOR).get_attribute('value')
        self.logger.debug('Create segment')
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)
        self.logger.info(f'''
            New segment created with name:
            {name}
            ''')
        return name

    @allure.step('Delete segment {name}')
    def delete_segment(self, name):
        self.logger.info('Segment deletion')
        segment_id = self.find(self.locators.ROW_LOCATOR(name)).get_attribute('href')
        self.logger.debug('Get segment id from herf')
        segment_id = segment_id[-1:-7]
        self.logger.debug(f'Delete segment with id={segment_id}')
        self.click(self.locators.MARK_ROW_LOCATOR(segment_id))
        self.click(self.locators.ACTIONS_LOCATOR)
        self.click(self.locators.DELETE_LOCATOR)

    @allure.step('Check segment {name}')
    def check_segment(self, name):
        self.logger.info('Segment check')
        try:
            self.find(self.locators.ROW_LOCATOR(name))
            self.logger.debug('Segment exist')
            return True
        except:
            self.logger.debug('Segment doesn\'t exist')
            return False