import pytest
import allure
from base import BaseCase


class Test(BaseCase):


    @pytest.mark.UI
    def test_login_incorrect(self): 
        log = 'login'
        psw = 'password'
        self.logger.info(f'Login in test')
        self.page.login(log='login', psw='password')
        self.logger.info('URL check')
        assert not self.page.url_check('https://target.my.com/dashboard')

    @pytest.mark.UI
    def test_login_nonexistent(self):
        log = 'password@pass.pass'
        psw = 'loginlogin'
        self.logger.debug(f'''
            Trying to login with:
            login: {log}
            password: {psw}
            ''')
        self.page.login(log=log, psw=psw)
        self.logger.info('URL check')
        assert not self.page.url_check('https://target.my.com/dashboard')

    @pytest.mark.UI
    def test_campaign(self, login, file_path):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'
        main_page = login
        campaign_page = main_page.open_campaign()
        self.logger.info(f'''
            Creating new campaign with
            URL: {url}
            ''')
        campaign_name = campaign_page.create_campaign(url, file_path)
        self.logger.info(f'''
            New campaign created with name:
            {campaign_name}
            ''')
        assert main_page.check_campaign(campaign_name)
        self.logger.info('Campaign deletion')
        main_page.delete_campaign(campaign_name)

    @pytest.mark.UI
    def test_create_segment(self, login):
        main_page = login
        segments_page = main_page.open_page('SEGMENTS')
        self.logger.info('Segment creation')
        segment_name = segments_page.create_segment()
        self.logger.info(f'''
            New segment created with name:
            {segment_name}
            ''')
        assert segments_page.check_segment(segment_name)
        self.logger.info('Segment deletion')
        segments_page.delete_segment(segment_name)

    @pytest.mark.UI
    def test_delete_segment(self, login):
        main_page = login
        segments_page = main_page.open_page('SEGMENTS')
        self.logger.info('Segment creation')
        segment_name = segments_page.create_segment()
        self.logger.info('Segment deletion')
        segments_page.delete_segment(segment_name)
        self.logger.info('Missing segment check')
        assert not segments_page.check_segment(segment_name)