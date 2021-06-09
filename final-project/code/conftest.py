import pytest
import os
import shutil
import allure
import logging
from selenium import webdriver
from api.client import ApiClient
from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='test_qa', password='qa_test', db_name='MYSQL_DB')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()

def pytest_addoption(parser):
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug_log')
    return {'debug_log': debug_log}

def pytest_configure(config):
    base_test_dir = 'tmp/tests'
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='test_qa', password='qa_test', db_name='MYSQL_DB')
        mysql_client.recreate_db()
        mysql_client.connect()
        mysql_client.create_table('test_users')
        mysql_client.connection.close()
        log = 'test_admin'
        psw = 'test_pass'
        email = 'test_admin@test.test'
        mysql_client.create_user(log, psw, email)

        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)
    config.base_test_dir = base_test_dir

@pytest.fixture(scope='function')
def test_dir(request):
    test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    caps = {'browserName': 'chrome',
            'version': '91.0',
            'sessionTimeout': '2m'}
    browser = webdriver.Remote('http://selenoid:4444/wd/hub', options=options, desired_capabilities=caps)
    browser.get("http://myapp:8080")
    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def api_client():
    log = 'test_admin'
    psw = 'test_pass'
    api_client = ApiClient()
    api_client.login(log, psw)
    yield api_client

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='function')
def file_path(repo_root):
    return os.path.join(repo_root, 'picture.png')

@pytest.fixture(scope='function')
def logger(config, test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-s - %(levelname)-s: %(message)s')
    log_file = os.path.join(test_dir, 'test.log')

    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)

@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_logfile = os.path.join(test_dir, 'browser.log')
        with open(browser_logfile, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_logfile, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

        log_file = os.path.join(test_dir, 'test.log')
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)

# @pytest.fixture(scope='function', autouse=True)
# def ui_report(driver, request, test_dir):
#     failed_tests_count = request.session.testsfailed
#     yield
#     if request.session.testsfailed > failed_tests_count:
#         screenshot_file = os.path.join(test_dir, 'failure.png')
#         driver.get_screenshot_as_file(screenshot_file)
#         allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

#         browser_logfile = os.path.join(test_dir, 'browser.log')
#         with open(browser_logfile, 'w') as f:
#             for i in driver.get_log('browser'):
#                 f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

#         with open(browser_logfile, 'r') as f:
#             allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)

#         log_file = os.path.join(test_dir, 'test.log')
#         if os.path.exists(log_file):
#             with open(log_file, 'r') as f:
#                 allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)