import pytest
import os
import allure
import shutil
import logging
from appium import webdriver
from capabilities import DESIRED_CAPS


def pytest_addoption(parser):
    parser.addoption('--debug_log', action='store_true')
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')

@pytest.fixture(scope='session')
def config(request):
    debug_log = request.config.getoption('--debug_log')
    appium = request.config.getoption('--appium')
    return {'debug_log': debug_log, 'appium': appium}

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
def driver(config):
    appium_url = config['appium']
    driver = webdriver.Remote(appium_url, desired_capabilities=DESIRED_CAPS)
    yield driver
    driver.quit()


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

        appium_logfile = os.path.join(test_dir, 'server.log')
        with open(appium_logfile, 'w') as f:
            for i in driver.get_log('server'):
                f.write(f"{i['message']}\n\n")
        with open(appium_logfile, 'r') as f:
            allure.attach(f.read(), 'server.log', attachment_type=allure.attachment_type.TEXT)

        log_file = os.path.join(test_dir, 'test.log')
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)