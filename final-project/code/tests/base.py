import pytest
import inspect
import requests
import random
from ui.pages.login_page import LoginPage


class BaseCase(object):

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client, api_client):
        self.mysql_client = mysql_client
        self.api_client = api_client

    @pytest.fixture(scope='function')
    def run_driver(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def make_user(self, log_cor=True, psw_cor=True, email_cor=True, rand_code=False):
        test_name = inspect.currentframe().f_back.f_code.co_name
        login =  test_name if log_cor else test_name[5:7]
        if rand_code:
            code = random.randint(1, 100)
        else: 
            code = 4 * log_cor + 2 * psw_cor + email_cor
        self.log = (str(code) + login)[:16]
        self.psw = 'test_pass' if psw_cor else ''
        self.email = self.log + '@test.test' if email_cor else self.log
        resp = requests.Session().get(f'http://vk_mock:5000/vk_id/{self.log}')
        if '404' in resp.json()['Status']:
            resp = requests.Session().post(f'http://vk_mock:5000/new_user/{self.log}')
        print(resp.json()['vk_id'])

    def check_url(self, url):
        res = False
        for frame in self.driver.window_handles:
            print(self.driver.current_url)
            self.driver.switch_to.window(frame)
            if url == self.driver.current_url:
                res = True
                break
        return res