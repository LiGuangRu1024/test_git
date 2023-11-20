# @time     ：2023/10/8 14:51
# @author   : 莉光哈哈哈
# @file     : test6_appium_web.py
# @software : PyCharm
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': '127.0.0.1:5555',
            # 'chromedriverExecutable': 'D:\\download\\appium\Appium - Server - GUI - windows - 1.22.2\\resources\\app\\node_modules\\appium\\node_modules\\appium - chromedriver\\chromedriver\\win'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        # sleep(5)
        self.driver.find_element(by=By.ID, value="index-kw").click()
        self.driver.find_element(by=By.ID, value="index-kw").send_keys("appium")
        search_locator = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(by=By.ID, value='*search_locator').click()


        # self.driver.quit()
