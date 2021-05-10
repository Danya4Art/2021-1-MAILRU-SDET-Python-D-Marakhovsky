import pytest
from client import ApiClient


class BaseCase(object):


    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.api_client = ApiClient()

    @pytest.fixture(scope='function')
    def login(self):
        cookies = self.api_client.login(self.user, self.password)
        assert cookies != None