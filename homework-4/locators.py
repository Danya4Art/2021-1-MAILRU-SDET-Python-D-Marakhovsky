from selenium.webdriver.common.by import By
from capabilities import DESIRED_CAPS

app = DESIRED_CAPS['appPackage']

class MainPageLocators(object):

    DENY_BUTTON = (By.ID, 'com.android.packageinstaller:id/permission_deny_button')
    KEYBOARD_BUTTON = (By.ID, f'{app}:id/keyboard')
    SEARCH_LINE = (By.ID, f'{app}:id/input_text')
    INPUT_BUTTON = (By.ID, f'{app}:id/text_input_send')
    CARD_LOCATOR = (By.ID, f'{app}:id/item_dialog_fact_card_content_text')
    ANSWER_LOCATOR = '//android.widget.TextView[@text="{}"]'
    ANSWER_LIST_LOCATOR = (By.ID,  f'{app}:id/suggests_list')
    RESULT_LOCATOR = (By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    BURGER_MENU = (By.ID, f'{app}:id/assistant_menu_bottom')

class SettingsPageLocators(object):
    NEWS_SOURCES = (By.ID, f'{app}:id/user_settings_field_news_sources')
    ABOUT_LOCATOR = (By.ID, f'{app}:id/user_settings_about')
    EXIT_LOCATOR = (By.XPATH, '//android.widget.LinearLayout/android.widget.ImageButton')

class SourcesPageLocators(object):
    VESTI_FM_LOCATOR = (By.XPATH, '//android.widget.TextView[@text="Вести FM"]/..')
    SELECTED_LOCATOR = (By.XPATH, '//android.widget.TextView[@text="Вести FM"]/../android.widget.ImageView')
    BACK_LOCATOR = (By.XPATH, '//android.widget.LinearLayout/android.widget.ImageButton')

class InfoPageLocators(object):
    VERSION_LOCATOR = (By.ID, f'{app}:id/about_version')
    ALL_RIGHTS_RESERVED_LOCATOR = (By.ID, f'{app}:id/about_copyright')

