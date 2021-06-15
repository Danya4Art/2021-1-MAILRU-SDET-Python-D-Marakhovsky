import logging
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    logger = logging.getLogger('test')


    class UrlCheck(object):

        def __init__(self, url):
            self.url = url
            
        def __call__(self, driver):
            self.logger.debug(f'''
                expected URL: {self.url}
                real URL: {driver.current_url}
                ''')
            if self.driver.current_url == self.url:
                self.logger.debug('URL correct')
                return self.url
            else:
                self.logger.debug('URL uncorrect')
                return False


    def __init__(self, driver):
        self.logger.info(f'{self.__class__.__name__} page is opening')
        self.driver = driver
        
    def find(self, locator, find_wait=3, invisibility=False):
        self.logger.debug(f'find element: {locator}')
        if invisibility:
            return self.driver.find_element(locator)
        elem = WebDriverWait(self.driver, find_wait).until(EC.presence_of_element_located(locator))
        return elem

    def click(self, locator, count=3, click_wait=1, find_wait=3):
        for i in range(count):
            try:
                elem = self.find(locator, find_wait=find_wait)
                self.logger.debug(f'click on element: {locator}')
                WebDriverWait(self.driver, click_wait).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except:
                if i == count - 1:
                    raise

    def enter(self, locator, key, find_wait=3):
        self.logger.debug(f'''
            send key: {key}
            to: {locator}
            ''')
        elem = self.find(locator, find_wait=find_wait)
        elem.send_keys(key)

    @allure.step('URL check')
    def url_check(self, url, check_wait=5):
        self.logger.info('URL check')
        try:
            return WebDriverWait(self.driver, check_wait).until(UrlCheck(url))
        except:
            return False

    @property
    def action_chains(self):
        return ActionChains(self.driver)