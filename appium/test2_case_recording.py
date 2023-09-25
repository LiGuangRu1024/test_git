# 时间：2023/9/13 14:10
# 人员: 莉光哈哈哈
import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {'platformName': 'Android', 'platformVersion': '7.1.2', 'deviceName': '127.0.0.1:7555',
                'appPackage': 'com.xueqiu.android', 'appActivity': '.view.WelcomeActivityAlias',
                "autoGrantPermissions": "true", 'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)  # 隐式等待

el1 = driver.find_element(by=By.ID, value="com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element(by=By.ID, value="com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
# el3 = driver.find_element(by=By.ID,
#                           value="com.xueqiu.android:id/action_close")
el3 = driver.find_element(by=By.XPATH,
                          value="//android.widget.TextView[@text='股票']")
el3.click()
el4 = driver.find_element(by=By.XPATH,
                          value="//android.widget.ListView[@resource-id='com.xueqiu.android:id/lv_list_view']/android.widget.RelativeLayout[1]")
el4.click()
time.sleep(3)  # 强制等待
driver.quit()
