from selenium.webdriver.common.by import By

class MainPageLocators:
    
    VK_ID_LOCATOR = (By.XPATH, '//li[contains(text(), "VK ID")]')
    USERNAME_LOCATOR = ((By.XPATH, '//li[contains(text(), "Logged as")]'))
    LOGOUT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
    FACT_LOCATOR = (By.XPATH, '//div/p[not(@style)]')
    # laptop https://en.wikipedia.org/wiki/API
    # loupe https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/
    # analytics https://ru.wikipedia.org/wiki/SMTP
    MIDDLE_ICONS_LOCATOR = '//img[@src="/static/images/{}.png"]/..' 
    # HOME http://0.0.0.0:8080/welcome/
    # Python https://www.python.org/
    # Linux  
    # Network 
    # Python history https://en.wikipedia.org/wiki/History_of_Python
    # About Flask https://flask.palletsprojects.com/en/1.1.x/#
    # Download Centos7 https://www.centos.org/download/
    # News https://www.wireshark.org/news/
    # Examples https://hackertarget.com/tcpdump-examples/ 
    # Download https://www.wireshark.org/#download
    TOP_PANEL_LOCATOR = '//a[text()="{}"]'
