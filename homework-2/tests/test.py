import pytest
import allure
from base import BaseCase


class Test(BaseCase):


    @allure.story('Log test')
    @pytest.mark.UI
    def test_login_incorrect(self): 
        log = 'login'
        psw = 'password'
        self.page.login(log='login', psw='password')
        assert not self.page.url_check('https://target.my.com/dashboard')

    @allure.story('Log test')
    @pytest.mark.UI
    def test_login_nonexistent(self):
        log = 'password@pass.pass'
        psw = 'loginlogin'
        self.page.login(log=log, psw=psw)
        assert not self.page.url_check('https://target.my.com/dashboard')

    @allure.story('Campaign test')
    @pytest.mark.UI
    def test_campaign(self, login, file_path):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'
        main_page = login
        campaign_page = main_page.open_page('CAMPAIGN')
        campaign_name = campaign_page.create_campaign(url, file_path)
        assert main_page.check_campaign(campaign_name)
        main_page.delete_campaign(campaign_name)

    @allure.story('Segment test')
    @pytest.mark.UI
    def test_create_segment(self, login):
        main_page = login
        segments_page = main_page.open_page('SEGMENTS')
        segment_name = segments_page.create_segment()
        assert segments_page.check_segment(segment_name)
        segments_page.delete_segment(segment_name)

    @allure.story('Segment test')
    @pytest.mark.UI
    def test_delete_segment(self, login):
        main_page = login
        segments_page = main_page.open_page('SEGMENTS')
        segment_name = segments_page.create_segment()
        segments_page.delete_segment(segment_name)
        assert not segments_page.check_segment(segment_name)