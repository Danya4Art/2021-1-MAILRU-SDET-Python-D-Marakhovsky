import pytest
from pages import *


class Test:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.start_page = StartPage(driver)
        self.main_page = MainPage(driver)
        self.profile_page = ProfilePage(driver)

    @pytest.mark.UI
    def test_login(self, driver):
        self.start_page.login()
        assert self.start_page.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self):
        self.start_page.login()
        self.main_page.logout()
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_profile(self):
        self.start_page.login()
        self.main_page.open_page('PROFILE')
        assert self.profile_page.change_data(
            fio='Abraham', num='1337', mail='abc@abc.abc'
        )

    # All possible values of i for parameterization:
    # 0 - АУДИТОРИИ
    # 1 - БАЛАНС
    # 2 - СТАТИСТИКА
    # 3 - PRO
    # 4 - ПРОФИЛЬ
    # 5 - ИНСТРУМЕНТЫ
    @pytest.mark.parametrize(
        'next_page, url_expected', 
        [(tags[i], urls[i]) for i in [1, 3]]
    )
    @pytest.mark.UI
    def test_parametrize_pages(self, next_page, url_expected):
        self.start_page.login()
        self.main_page.open_page(next_page)
        assert self.driver.current_url in url_expected