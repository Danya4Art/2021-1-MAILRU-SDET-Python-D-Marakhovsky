import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    # Set webdriver path
    browser = webdriver.Chrome(executable_path='')
    browser.maximize_window()
    browser.get("https://target.my.com")
    yield browser
    browser.close()