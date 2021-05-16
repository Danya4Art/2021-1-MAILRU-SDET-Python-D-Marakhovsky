import logging
import allure
import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class BasePage(object):

    logger = logging.getLogger('test')

    def __init__(self, driver):
        self.logger.info(f'{self.__class__.__name__} page is opening')
        self.driver = driver

    def find(self, locator, find_wait=3, invisibility=False):
        self.logger.debug(f'find element: {locator}')
        return WebDriverWait(self.driver, timeout=find_wait).until(EC.presence_of_element_located(locator))

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

    @staticmethod
    def get_central_coor(elem):
        coor = re.findall(
                         r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', 
                         elem.get_attribute('bounds')
                         )
        return {
               'x': (int(coor[0][0]) + int(coor[0][2])) // 2,
               'y': (int(coor[0][1]) + int(coor[0][3])) // 2,
               }

    def swipe_to_element(self, locator, position='below', swipe_elem=None, max_swipes=3, swipetime=200):
        self.logger.debug(f'Swipe to element: {locator} located on {position}') 
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        if position == 'below':
            start = {
            'x': int(dimension['width'] / 2),
            'y': int(dimension['height'] * 0.8)
            }
            end = {
            'x': int(dimension['width'] / 2),
            'y': int(dimension['height'] * 0.2)
            }
        elif position == 'above':
            start = {
            'x': int(dimension['width'] / 2),
            'y': int(dimension['height'] * 0.2)
            }
            end = {
            'x': int(dimension['width'] / 2),
            'y': int(dimension['height'] * 0.8)
            }
        elif position == 'right' and swipe_elem != None:
            start = {
            'x': int(dimension['width'] * 0.8),
            'y': self.get_central_coor(swipe_elem)['y']
            }
            end = {
            'x': int(dimension['width'] * 0.2),
            'y': self.get_central_coor(swipe_elem)['y']
            }
        elif position == 'left' and swipe_elem != None:
            start = {
            'x': int(dimension['width'] * 0.2),
            'y': self.get_central_coor(swipe_elem)['y']
            }
            end = {
            'x': int(dimension['width'] * 0.8),
            'y': self.get_central_coor(swipe_elem)['y']
            }
        else:
            raise ValueError('Invalid position')
        self.logger.debug(f'Coordinates:\nstart = {start}\nend = {end}') 
        for i in range(max_swipes + 1):
            try: 
                WebDriverWait(self.driver, timeout=0).until(EC.visibility_of_element_located(locator))
                return
            except:
                pass
            action. \
                press(x=start['x'], y=start['y']). \
                wait(ms=swipetime). \
                move_to(x=end['x'], y=end['y']). \
                release(). \
                perform()
        raise  