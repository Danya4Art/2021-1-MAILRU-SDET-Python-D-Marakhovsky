import os

def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

def file_path():
    return os.path.join(repo_root(), 'stuff/Marussia_v1.39.1.apk')

DESIRED_CAPS = {
"platformName": "Android",
"platformVersion": "8.1",
"automationName": "Appium",
"appPackage": "ru.mail.search.electroscope",
"appActivity": "ru.mail.search.electroscope.ui.activity.AssistantActivity",
"app": file_path(),
"orientation": "PORTRAIT",
"autoGrantPermissions": "true"
}