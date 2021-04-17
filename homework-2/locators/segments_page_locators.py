from locators.top_panel_locators import TopPanelLocators
from selenium.webdriver.common.by import By


class SegmentsPageLocators(TopPanelLocators):
    NEW_SEGMENT_LOCATOR = [
    (By.XPATH, '//*[@href="/segments/segments_list/new/"]'),
    (By.XPATH, '//*[contains(@class,"segments-list__btn-wrap")]/button')
    ]
    APPS_LOCATOR = (By.XPATH, '//div[text()="Приложения и игры в соцсетях"]')
    PLAY_PAY_LOCATOR = (By.XPATH, '//*[contains(@class, "adding-segments-source__header")]')
    MARK_PAY_LOCATOR = (By.XPATH, '//input[@value="pay"]')
    ADD_SEGMENT_LOCATOR = (By.XPATH, '//*[contains(@class,"js-add-button")]/button')
    CREATE_SEGMENT_LOCATOR = (By.XPATH, '//*[contains(@class,"js-create-segment-button-wrap")]/button')
    NAME_LOCATOR = (By.XPATH, '//*[@class="input__wrap"]/input[@maxlength="60"]')
    ACTIONS_LOCATOR = (By.XPATH, '//*[@data-test="select" and contains(@class, "segmentsTable")]')
    DELETE_LOCATOR = (By.XPATH, '//*[@data-id="remove"]')

    @staticmethod
    def ROW_LOCATOR(name):
        return (By.XPATH, f'//a[@title="{name}"]')

    @staticmethod
    def MARK_ROW_LOCATOR(segment_id):
        return (By.XPATH, f'//*[contains(@data-test, "id-{segment_id}")]//input')