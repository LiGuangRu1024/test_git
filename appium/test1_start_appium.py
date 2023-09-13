# 时间：2023/9/13 10:26
# 人员: 莉光哈哈哈
import time

from appium import webdriver

desired_caps = {'platformName': 'Android', 'platformVersion': '12.0', 'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.android.settings', 'appActivity': 'com.android.settings.Settings'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(10)
driver.quit()
