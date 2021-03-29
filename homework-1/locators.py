from selenium.webdriver.common.by import By
from top_panel import tags, href

class StartPageLocators:
    BUTTON_LOCATOR = (By.XPATH, '//*[@class="js-target-content-react"]//div[(text()="Войти")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOCATOR = (By.XPATH, '//*[@class="js-target-common-modals"]//div[(text()="Войти")]')


class MainPageLocators:
    RIGHT_MODULE_LOCATOR = (By.XPATH, '//*[starts-with(@class, "right-module-rightButton")]')
    BUTTONS_LOCATORS = {tags[i]: (By.XPATH, href[i]) for i in range(len(tags))}


class ProfilePageLocators(MainPageLocators):
    FIO_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
    PHONE_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
    MAIL_LOCATOR = (By.XPATH, '//li[@class="profile__list__row profile__list__row_emails"]//input')
    CONFIRM_LOCATOR = (By.TAG_NAME, 'button')
    SUCCESS_LOCATOR = (By.XPATH, '//div[@data-class-name="SuccessView"]')