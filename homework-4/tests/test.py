import pytest
import allure
from base import BaseCase


class Test(BaseCase):


    @allure.story('Chat test')
    @pytest.mark.AndroidUI
    def test_russia(self):
        self.main_page.search_russia()

    @allure.story('Chat test')
    @pytest.mark.AndroidUI
    @pytest.mark.parametrize(
        'expression, result_expected', 
        [
        ('3+5', 8)
        ]
    )
    def test_calc(self, expression, result_expected):
        assert result_expected == self.main_page.calculate(expression)

    @allure.story('Source test')
    @pytest.mark.AndroidUI
    def test_news(self):
        settings_page = self.main_page.open_settings()
        sources_page = settings_page.open_sources()
        sources_page.select_vesti()
        settings_page.back_to_main_page()
        self.main_page.check_vesti()

    @allure.story('Info test')
    @pytest.mark.AndroidUI
    def test_info(self):
        settings_page = self.main_page.open_settings()
        info_page = settings_page.open_info()
        info_page.check_info()