from selenium.webdriver.common.by import By


class StartPageLocators:
    BUTTON_LOCATOR = (By.XPATH, '//*[@class="js-target-content-react"]//div[(text()="Войти")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOCATOR = (By.XPATH, '//*[@class="js-target-common-modals"]//div[(text()="Войти")]')