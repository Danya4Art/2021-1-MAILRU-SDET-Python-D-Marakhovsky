import pytest
import os
import allure
import shutil
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--log', default='vibamel876@ichkoch.com')
    parser.addoption('--psw', default='yJW6j3rbtNAW8cw')
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    log = request.config.getoption('--log')
    psw = request.config.getoption('--psw')
    debug_log = request.config.getoption('--debug_log')
    return {'log': log, 'psw': psw, 'debug_log': debug_log}

def is_master(config):
    if hasattr(config, 'workerinput'):
        return False
    return True

def pytest_configure(config):
    base_test_dir = 'tmp/tests'
    if is_master:
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

@pytest.fixture(scope='function', autouse=True)
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