# 时间：2023/6/19 16:27
# 人员: 莉光哈哈哈

'''
强制等待
    使用方法：time.sleep(秒数)
    程序遇到time.sleep停止运行，时间一到再开始运行
'''

'''
    implicitly_wait()秒
    隐性等待：
    设置一个最长等待时间，如果在规定内，网页加载完成，执行下一步
    否则一直等到时间截止，然后执行下一步（程序会一直等待整个页面加载完成）
'''

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.implicitly_wait(30)
    driver.find_element(by=By.CSS_SELECTOR, value='#searchKey').send_keys("爱在大雾散尽时")
    time.sleep(1)
    driver.find_element(by=By.ID, value='btnSearch').click()
    time.sleep(3)


