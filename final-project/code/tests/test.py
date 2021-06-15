import pytest
import allure
from base import BaseCase
from time import sleep

three_bit = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]

class TestApi(BaseCase):

    @allure.story('Create user test')
    @pytest.mark.parametrize('log, psw, email', [
            (0, 0, 0),
            (1, 1, 1)
      ])
    def test_add_user(self, log, psw, email):
        res = log * psw * email
        self.make_user(log, psw, email)
        self.api_client.create_user(self.log, self.psw, self.email)
        assert int(self.mysql_client.user_exist(self.log)) == res

    @allure.story('Delete user test')
    def test_del_user(self):
        self.make_user()
        self.mysql_client.create_user(self.log, self.psw, self.email)
        self.api_client.delete_user(self.log)
        assert self.mysql_client.user_exist(self.log) == False

    @allure.story('Block user test')
    def test_block_user(self):
        self.make_user()
        self.mysql_client.create_user(self.log, self.psw, self.email)
        self.api_client.block_user(self.log)
        assert self.mysql_client.get_user(self.log).access == 0

    @allure.story('Accept user test')
    def test_accept_user(self):
        self.make_user()
        self.mysql_client.create_user(self.log, self.psw, self.email)
        self.api_client.block_user(self.log)
        self.api_client.accept_user(self.log)
        assert self.mysql_client.get_user(self.log).access == 1

    @allure.story('Status test')
    def test_status(self):
        predict = {"status": "ok"}
        assert predict == self.api_client.status()


class TestUI(BaseCase):

    @pytest.fixture(scope='function', autouse=True)
    def setup_driver(self, run_driver):
        pass

    @allure.story('Create user test')
    def test_register(self):
        self.make_user()
        reg_page = self.login_page.open_registration_page()
        main_page = reg_page.registrate(self.log, self.email, self.psw)
        self.mysql_client.session_commit()
        assert self.mysql_client.user_exist(self.log) == True
        assert 'http://selenoid:8080/welcome/' == self.driver.current_url

    @allure.story('Login test')
    def test_login(self):
        self.make_user()
        self.mysql_client.create_user(self.log, self.psw, self.email)
        main_page = self.login_page.login(self.log, self.psw)
        assert 'http://selenoid:8080/welcome/' == self.driver.current_url

    @allure.story('Login test')
    def test_login_api(self):
        self.make_user()
        self.mysql_client.create_user(self.log, self.psw, self.email)
        cookies = self.api_client.login(self.log, self.psw)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('http://127.0.0.1:8080/welcome/')
        assert 'http://selenoid:8080/welcome/' == self.driver.current_url
    
    @allure.story('Main page test')
    @pytest.mark.parametrize('name, url',[
        ('laptop', 'https://en.wikipedia.org/wiki/API'),
        ('loupe', 'https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/'),
        ('analytics', 'https://ru.wikipedia.org/wiki/SMTP')
    ])
    def test_middle_icons(self, name, url):
        self.make_user(rand_code=True)
        self.mysql_client.create_user(self.log, self.psw, self.email)
        main_page = self.login_page.login(self.log, self.psw)
        main_page.open_middle_icons(name)
        sleep(3)
        assert self.check_url(url)

    @allure.story('Main page test')
    @pytest.mark.parametrize('name, url', [
        ('HOME', 'http://selenoid:8080/welcome/'),
        ('Python', 'https://www.python.org/'),
        ('Python history', 'https://en.wikipedia.org/wiki/History_of_Python'),
        ('About Flask', 'https://flask.palletsprojects.com/en/1.1.x/#'),
        ('Download Centos7', 'https://www.centos.org/download/'),
        ('News', 'https://www.wireshark.org/news/'),
        ('Examples ', 'https://hackertarget.com/tcpdump-examples/'),
        ('Download', 'https://www.wireshark.org/#download')
    ])
    def test_top_panel(self, name, url):
        self.make_user(rand_code=True)
        self.mysql_client.create_user(self.log, self.psw, self.email)
        main_page = self.login_page.login(self.log, self.psw)
        main_page.open_top_panel(name)
        sleep(3)
        assert self.check_url(url)
        