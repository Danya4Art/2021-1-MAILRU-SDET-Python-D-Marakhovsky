import pytest
from client import ApiClient


class BaseCase(object):

    open_browser = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.api_client = ApiClient()
        if self.open_browser:
            self.driver = driver

    @pytest.fixture(scope='function')
    def login(self):
        cookies = self.api_client.login(self.user, self.password)
        assert cookies != None
        if self.open_browser:
	        for c in cookies:
	            self.driver.add_cookie(c)