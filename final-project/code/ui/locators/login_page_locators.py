from selenium.webdriver.common.by import By

class LoginPageLocators:

    USERNAME_LOCATOR = (By.ID, 'username')
    PASSWORD_LOCATOR = (By.ID, 'password')
    SUBMIT_LOCATOR = (By.ID, 'submit')
    CHANGE_PAGE_LOCATOR = '//a[@href="/{}"]'
    