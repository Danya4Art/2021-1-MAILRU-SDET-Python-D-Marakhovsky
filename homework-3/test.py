import requests
import pytest
from _pytest.fixtures import FixtureRequest
from requests.cookies import cookiejar_from_dict
from time import sleep
from base import BaseCase


class Test(BaseCase): 

    user = 'makoci4336@zcai55.com'
    password = 'Njgfv3YLC2G7QmD'

    def test_login(self, login):
        if self.open_browser:
            self.driver.get('https://target.my.com/dashboard')
        sleep(3)

    def test_campaign(self, login, file_path):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO'
        campaign_id = self.api_client.create_campaign(file_path, url)
        if self.open_browser:
            self.driver.get('https://target.my.com/dashboard')
        sleep(3)
        # Далее ошибка
        try:
            self.api_client.delete_campaign(campaign_id)
        except:
            print('Deletion error') 

    # Этот тест упадет
    def test_create_segment(self, login):
        segment_id = self.api_client.create_segment()
        if self.open_browser:
            self.driver.get('https://target.my.com/segments/segments_list')
        sleep(3)
        self.api_client.delete_segment(segment_id)

    # Этот тоже
    def test_delete_segment(self, login):
        segment_id = self.api_client.create_segment()
        if self.open_browser:
            self.driver.get('https://target.my.com/segments/segments_list')
        sleep(3)
        self.api_client.delete_segment(segment_id)