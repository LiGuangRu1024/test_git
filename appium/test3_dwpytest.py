# 时间：2023/9/18 16:51
# 人员: 莉光哈哈哈
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestDW:
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
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search").click()
        self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(by=By.XPATH, value="//android.widget.TextView[@text='股票']").click()
        self.driver.find_element(by=By.XPATH,
                                 value="//android.widget.ListView[@resource-id='com.xueqiu.android:id/lv_list_view']/android.widget.RelativeLayout[1]").click()

    def test_attr(self):
        '''
        打开【雪球】应用首页
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”点击，如果不可见，打印“搜索失败”
        :return:
        '''
        element = self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled:
            element.click()
            self.driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            self.driver.find_element(by=By.XPATH, value="//android.widget.TextView[@text='股票']").click()
            alibaba_element = self.driver.find_element(by=By.XPATH,
                                                       value="//android.widget.ListView[@resource-id='com.xueqiu.android:id/lv_list_view']/android.widget.RelativeLayout[1]")
            element_displayed = alibaba_element.get_attribute("displayed")
            if element_displayed == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchAction(self):
        action = TouchAction(self.driver)
        # print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()

    # def test_touchAction_1(self):
    #     print("解锁手势密码")


if __name__ == '__main__':
    pytest.main()
