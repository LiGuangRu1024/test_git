# @time     ：2023/10/8 16:35
# @author   : 莉光哈哈哈
# @file     : test7_interact.py
# @software : PyCharm
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestInteract:
    def setup(self):
        des_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': '127.0.0.1:5555',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            "autoGrantPermissions": "true",
            'noReset': True,
            'unicodeKeyBoard': 'true',
            'resetKeyBoard': 'true'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_mobile_interact(self):
        self.driver.make_gsm_call('16895445694', GsmCallActions.CALL)
        self.driver.send_sms('16996596546', 'hello appium api')
        self.driver.set_network_connection(1)
        sleep(3)
        self.driver.get_screenshot_as_file('./photos/img.png')
        self.driver.set_network_connection(4)
        sleep(3)

