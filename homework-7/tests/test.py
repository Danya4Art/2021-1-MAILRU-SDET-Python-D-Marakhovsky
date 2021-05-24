import requests
import pytest
import settings
from mock.flask_mock import SURNAME_DATA
from decision.socket_client import Client


class Base():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
        self.url_mock = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'
        self.client = Client()


class Test(Base):

    def test_put_mock(self):
        name = 'Igor'
        SURNAME_DATA[name] = 'Zaitcev'
        requests.put(f'{self.url_mock}/rewrite/{name}', json={'surname': 'Okopyan'})
        assert SURNAME_DATA[name] == 'Okopyan'     

    def test_delete_mock(self):
        name = 'Vitaly'
        SURNAME_DATA[name] = 'Zaitcev'
        requests.delete(f'{self.url_mock}/delete/{name}')
        assert name not in SURNAME_DATA.keys()

    def test_soket_get(self):
        name = 'Cat'
        SURNAME_DATA[name] = 'Zaitcev'
        requests.post(f'{self.url}/add_user', json={'name': name})
        assert 'Zaitcev' in self.client.get_surname_by_name(name)