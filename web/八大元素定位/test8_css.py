# 时间：2023/6/19 15:48
# 人员: 莉光哈哈哈


import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.CSS_SELECTOR, value='#searchKey').send_keys("爱在大雾散尽时")
    time.sleep(1)
    driver.find_element(by=By.ID, value='btnSearch').click()
    time.sleep(3)


