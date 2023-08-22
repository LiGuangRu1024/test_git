# 时间：2023/6/19 11:03
# 人员: 莉光哈哈哈

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="录")
    time.sleep(1)
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="录").click()
    time.sleep(3)
