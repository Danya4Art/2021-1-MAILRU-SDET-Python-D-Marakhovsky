import pytest
from pages.main_page import MainPage


class BaseCase(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger):
        self.logger = logger
        self.logger.info('Connect to appium')
        self.driver = driver
        self.main_page = MainPage(driver)