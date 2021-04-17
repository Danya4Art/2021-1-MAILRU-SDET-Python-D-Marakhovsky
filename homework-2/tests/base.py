import pytest
from pages.start_page import StartPage


class BaseCase(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger):
        self.logger = logger
        self.logger.info('Open browser')
        self.driver = driver
        self.page = StartPage(driver)

    @pytest.fixture(scope='function')
    def login(self, driver, config):
        self.logger.info('Login in fixture')
        main_page = self.page.login(config['log'], config['psw'])
        return main_page