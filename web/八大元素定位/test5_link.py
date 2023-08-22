# 时间：2023/6/19 10:53
# 人员: 莉光哈哈哈


'''
针对文本链接的。可以不用管标签，直接通过文本就能定位
'''

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.LINK_TEXT, value="登录")
    time.sleep(1)
    driver.find_element(by=By.LINK_TEXT, value="登录").click()
    time.sleep(3)
