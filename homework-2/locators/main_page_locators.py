from locators.top_panel_locators import TopPanelLocators
from selenium.webdriver.common.by import By


class MainPageLocators(TopPanelLocators):
    TopPanelLocators.BUTTONS_LOCATORS['CAMPAIGN'] = (By.XPATH,
     '''//*[starts-with(@class, "dashboard-module-createButtonWrap")]/div | 
        //*[@href="/campaign/new"]''')
    MARK_ALL_LOCATOR = (By.XPATH, '//input[starts-with(@class, "name-module-checkbox")]')
    ACTIONS_LOCATOR = (By.XPATH, '//*[starts-with(@class, "tableControls-module-massActionsSelect")]')
    DELETE_LOCATOR = (By.XPATH, '//*[@title="Удалить"]')

    @staticmethod
    def MARK_CAMPAIGN_LOCATOR(name):
        return (By.XPATH, f'//*[text()="{name}"]/../input')