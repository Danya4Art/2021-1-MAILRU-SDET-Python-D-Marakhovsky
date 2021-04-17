from locators.top_panel_locators import TopPanelLocators
from selenium.webdriver.common.by import By


class CampaignPageLocators(TopPanelLocators):
    TRAFFIC_LOCATOR = (By.XPATH, '//*[contains(@class, "_traffic")]')
    LINK_LOCATOR = (By.XPATH, '//*[contains(@data-gtm-id, "ad_url_text")]')
    NAME_LOCATOR = (By.XPATH, '//*[@class="input__wrap"]/input[@maxlength="255"]')
    BANNER_LOCATOR = (By.ID, 'patterns_4')
    IMAGE_LOCATOR = (By.XPATH, '//*[starts-with(@class,"upload-module-dropArea")]')
    INPUT_LOCATOR = (By.XPATH, '//input[@data-test="image_240x400" and @type="file"]')    
    SAVE_LOCATOR = (By.XPATH, '//*[@data-test="submit_banner_button"]')
    CREATE_LOCATOR = (By.XPATH, '//*[@data-service-readonly="true"]')