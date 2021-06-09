from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    
    locators = MainPageLocators()

    def open_middle_icons(self, name):
        self.click((By.XPATH, self.locators.MIDDLE_ICONS_LOCATOR.format(name)))

    def open_top_panel(self, name):
        dropdown = ''
        if name in ['Python history', 'About Flask']:
            dropdown = 'Python'
        elif name in ['Download Centos 7']:
            dropdown = 'Linux'
        elif name in ['News', 'Examples', 'Download']:
            dropdown = 'Network'
        elif name in ['HOME', 'Python', 'Linux', 'Network']:
            self.click((By.XPATH, self.locators.TOP_PANEL_LOCATOR.format(name)))
            return
        else:
            return None
        self.action_chains \
        .move_to_element(self.find((By.XPATH, self.locators.TOP_PANEL_LOCATOR.format(dropdown)))) \
        .pause(1).perform()
        self.click((By.XPATH, self.locators.TOP_PANEL_LOCATOR.format(name)))

    def get_username(self):
        username = self.find(self.locators.USERNAME_LOCATOR).get_attribute('text')
        res = username.split(' ')[2]
        return res

    def get_vk_id(self):
        username = self.find(self.locators.VK_ID_LOCATOR).get_attribute('text')
        res = username.split(' ')[2]
        return res