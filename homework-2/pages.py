import logging
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LOCATORS

logger = logging.getLogger('test')


class BasePage(object):


    class UrlCheck(object):

        def __init__(self, url):
            self.url = url
            
        def __call__(self, driver):
            logger.debug(f'''
                expected URL: {self.url}
                real URL: {driver.current_url}
                ''')
            if driver.current_url == self.url:
                logger.debug('URL correct')
                return self.url
            else:
                logger.debug('URL uncorrect')
                return False


    def __init__(self, driver):
        logger.info(f'{self.__class__.__name__} page is opening')
        self.driver = driver
        
    def find(self, locator, find_wait=3, invisibility=False):
        logger.debug(f'find element: {locator}')
        if invisibility:
            return self.driver.find_element(locator)
        elem = WebDriverWait(self.driver, find_wait).until(EC.presence_of_element_located(locator))
        return elem

    def click(self, locator, count=3, click_wait=1, find_wait=3):
        for i in range(count):
            try:
                elem = self.find(locator, find_wait=find_wait)
                logger.debug(f'click on element: {locator}')
                WebDriverWait(self.driver, click_wait).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except:
                if i == count - 1:
                    raise

    def enter(self, locator, key, find_wait=3):
        logger.debug(f'''
            send key: {key}
            to: {locator}
            ''')
        elem = self.find(locator, find_wait=find_wait)
        elem.send_keys(key)

    @allure.step('URL check')
    def url_check(self, url, check_wait=5):
        try:
            return WebDriverWait(self.driver, check_wait).until(UrlCheck(url))
        except:
            return False

    @property
    def action_chains(self):
        return ActionChains(self.driver)


class StartPage(BasePage):

    locators = LOCATORS['StartPage']

    @allure.step('Login')
    def login(self, log, psw):
        logger.info(f'''
            login: {log}
            password: {psw}
            ''')
        self.click(self.locators.BUTTON_LOCATOR)
        self.enter(self.locators.EMAIL_LOCATOR, log)
        self.enter(self.locators.PASSWORD_LOCATOR, psw)
        self.click(self.locators.ENTER_LOCATOR)
        return MainPage(self.driver)


class MainPage(BasePage):

    locators = LOCATORS['MainPage']

    @allure.step('Logout')
    def logout(self):
        logger.debug('Logout')
        self.click(self.locators.RIGHT_MODULE_LOCATOR)
        self.click(self.locators.BUTTONS_LOCATORS['LOGOUT'])
        return StartPage(self.driver)

    @allure.step('Open {new_page} page')
    def open_page(self, new_page):
        logger.debug(f'Open {new_page} page')
        self.click(self.locators.BUTTONS_LOCATORS[new_page])
        if new_page == 'SEGMENTS':
            return SegmentsPage(self.driver)    

    def open_campaign(self):
        logger.debug('Open campaign page')
        self.click(self.locators.NEW_CAMPAIGN_LOCATOR)
        return CampaignPage(self.driver)

    @allure.step('Delete campaign {name}')
    def delete_campaign(self, name, every=False):
        if every:
            logger.debug('Delete all campaigns')
            self.click(self.locators.MARK_ALL_LOCATOR)
        else:
            logger.debug(f'Delete {name} campaign')
            campaign_mark = self.locators.MARK_CAMPAIGN_LOCATOR(name)
            self.click(campaign_mark)
        self.click(self.locators.ACTIONS_LOCATOR)
        self.click(self.locators.DELETE_LOCATOR)

    @allure.step('Check campaign {name}')
    def check_campaign(self, name):
        try:
            self.find(self.locators.MARK_CAMPAIGN_LOCATOR(name), find_wait=10)
            logger.debug('Campaign exist')
            return True
        except:
            logger.debug('Campaign doesn\'t exist')
            return False


class CampaignPage(MainPage):

    locators = LOCATORS['CampaignPage']

    @allure.step('Create campaign')
    def create_campaign(self, link, image):
        logger.debug('Choose traffic type')
        self.click(self.locators.TRAFFIC_LOCATOR)
        logger.debug('Paste link')
        self.enter(self.locators.LINK_LOCATOR, link)
        name = self.find(self.locators.NAME_LOCATOR).get_attribute('value')
        logger.debug('Scroll to banner')
        self.action_chains.move_to_element(self.find(self.locators.BANNER_LOCATOR)).click().perform()
        logger.debug('Scroll to picture place')
        self.action_chains.move_to_element(self.find(self.locators.IMAGE_LOCATOR)).perform()
        self.enter(self.locators.INPUT_LOCATOR, image)
        self.click(self.locators.CREATE_LOCATOR)
        return name


class SegmentsPage(MainPage):

    locators = LOCATORS['SegmentsPage']

    @allure.step('Create segment')
    def create_segment(self):
        try:
            self.click(self.locators.NEW_SEGMENT_LOCATOR[0])
        except:
            self.click(self.locators.NEW_SEGMENT_LOCATOR[1])
        logger.debug('Segment settings')
        self.click(self.locators.APPS_LOCATOR)
        self.click(self.locators.PLAY_PAY_LOCATOR)
        self.click(self.locators.MARK_PAY_LOCATOR)
        self.click(self.locators.ADD_SEGMENT_LOCATOR)
        logger.debug('Get segment name')
        name = self.find(self.locators.NAME_LOCATOR).get_attribute('value')
        logger.debug('Create segment')
        self.click(self.locators.CREATE_SEGMENT_LOCATOR)
        return name

    @allure.step('Delete segment {name}')
    def delete_segment(self, name):
        segment_id = self.find(self.locators.ROW_LOCATOR(name)).get_attribute('href')
        logger.debug('Get segment id from herf')
        segment_id = segment_id[-1:-7]
        logger.debug(f'Delete segment with id={segment_id}')
        self.click(self.locators.MARK_ROW_LOCATOR(segment_id))
        self.click(self.locators.ACTIONS_LOCATOR)
        self.click(self.locators.DELETE_LOCATOR)

    @allure.step('Check segment {name}')
    def check_segment(self, name):
        try:
            self.find(self.locators.ROW_LOCATOR(name))
            logger.debug('Segment exist')
            return True
        except:
            logger.debug('Segment doesn\'t exist')
            return False