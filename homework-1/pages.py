from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        
    def find(self, locator, find_wait=5):
        elem = WebDriverWait(self.driver, find_wait).until(EC.visibility_of_element_located(locator))
        return elem

    def click(self, locator, count=3, click_wait=5, find_wait=5):
        for i in range(count):
            try:
                elem = self.find(locator, find_wait=find_wait)
                WebDriverWait(self.driver, click_wait).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except:
                if i == count:
                    raise

    def enter(self, locator, key):
        elem = self.find(locator)
        elem.send_keys(key)


class StartPage(BasePage):

    locators = StartPageLocators()
    user_login = 'vibamel876@ichkoch.com'
    user_password = 'yJW6j3rbtNAW8cw'

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, log=user_login, psw=user_password):
        self.click(self.locators.BUTTON_LOCATOR)
        self.enter(self.locators.EMAIL_LOCATOR, log)
        self.enter(self.locators.PASSWORD_LOCATOR, psw)
        self.click(self.locators.ENTER_LOCATOR)


class MainPage(BasePage):

    locators = MainPageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click(self.locators.RIGHT_MODULE_LOCATOR)
        self.click(self.locators.BUTTONS_LOCATORS['LOGOUT'])

    def open_page(self, new_page):
        self.click(self.locators.BUTTONS_LOCATORS[new_page])



class ProfilePage(MainPage):

    locators = ProfilePageLocators()

    def __init__(self, driver):
        super().__init__(driver)

    def change_data(self, fio=None, num=None, mail=None):
        if fio == None and num == None and mail == None:
            return False
        if fio != None:
            self.find(self.locators.FIO_LOCATOR).clear()
            self.enter(self.locators.FIO_LOCATOR, fio)
        if num != None:
            self.find(self.locators.PHONE_LOCATOR).clear()
            self.enter(self.locators.PHONE_LOCATOR, num)
        if mail != None:
            self.find(self.locators.MAIL_LOCATOR).clear()
            self.enter(self.locators.MAIL_LOCATOR, mail)
        self.click(self.locators.CONFIRM_LOCATOR)
        try:
            self.find(self.locators.SUCCESS_LOCATOR)
            return True
        except:
            return False