import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def driver():
    os.environ['WDM_LOG_LEVEL'] = '0'
    manager = ChromeDriverManager(version='latest')
    browser = webdriver.Chrome(executable_path=manager.install())
    browser.maximize_window()
    browser.get("https://target.my.com")
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, 'picture.png')