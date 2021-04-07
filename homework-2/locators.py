from selenium.webdriver.common.by import By
from top_panel import tags, href


class StartPageLocators:
    BUTTON_LOCATOR = (By.XPATH, '//*[@class="js-target-content-react"]//div[(text()="Войти")]')
    EMAIL_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    ENTER_LOCATOR = (By.XPATH, '//*[@class="js-target-common-modals"]//div[(text()="Войти")]')


class TopPanelLocators:
    RIGHT_MODULE_LOCATOR = (By.XPATH, '//*[starts-with(@class, "right-module-rightButton")]')
    BUTTONS_LOCATORS = {tags[i]: (By.XPATH, href[i]) for i in range(len(tags))}


class MainPageLocators(TopPanelLocators):
    MARK_ALL_LOCATOR = (By.XPATH, '//input[starts-with(@class, "name-module-checkbox")]')
    NEW_CAMPAIGN_LOCATOR = (By.XPATH, '''//*[starts-with(@class, "dashboard-module-createButtonWrap")]/div | 
                                         //*[@href="/campaign/new"]''')
    ACTIONS_LOCATOR = (By.XPATH, '//*[starts-with(@class, "tableControls-module-massActionsSelect")]')
    DELETE_LOCATOR = (By.XPATH, '//*[@title="Удалить"]')

    @staticmethod
    def MARK_CAMPAIGN_LOCATOR(name):
        return (By.XPATH, f'//*[text()="{name}"]/../input')


class CampaignPageLocators(TopPanelLocators):
    TRAFFIC_LOCATOR = (By.XPATH, '//*[contains(@class, "_traffic")]')
    LINK_LOCATOR = (By.XPATH, '//*[contains(@data-gtm-id, "ad_url_text")]')
    NAME_LOCATOR = (By.XPATH, '//*[@class="input__wrap"]/input[@maxlength="255"]')
    BANNER_LOCATOR = (By.ID, 'patterns_4')
    IMAGE_LOCATOR = (By.XPATH, '//*[starts-with(@class,"upload-module-dropArea")]')
    INPUT_LOCATOR = (By.XPATH, '//input[@data-test="image_240x400" and @type="file"]')    
    SAVE_LOCATOR = (By.XPATH, '//*[@data-test="submit_banner_button"]')
    CREATE_LOCATOR = (By.XPATH, '//*[@data-service-readonly="true"]')


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


LOCATORS = {
'StartPage': StartPageLocators(),
'MainPage': MainPageLocators(),
'CampaignPage': CampaignPageLocators(),
'SegmentsPage': SegmentsPageLocators()
}