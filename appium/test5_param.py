# 时间：2023/9/27 10:46
# 人员: 莉光哈哈哈
import time

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *


class TestParam:

    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1.2',
                        'deviceName': '127.0.0.1:7555',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': '.view.WelcomeActivityAlias',
                        "autoGrantPermissions": "true",
                        'noReset': True,
                        'unicodeKeyBoard': 'true',
                        'resetKeyBoard': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 隐式等待

    def teardown(self):
        pass

    @pytest.mark.parametrize("keys, text", [
        ("阿里巴巴", "股票"),
        ("爱奇艺", "组合")
    ])
    def test_search(self, keys, text):
        """
        1、打开雪球
        2、点击搜索框
        3、输入搜索词
        :return:
        """
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys(keys)
        self.driver.find_element(by=By.XPATH, value=f"//android.widget.TextView[@text='{text}']").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/stockName").click()
        # current_name = self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/stockName")
        # assert_that(current_name), contains_string("阿里巴巴"))
