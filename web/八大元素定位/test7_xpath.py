# 时间：2023/6/19 11:08
# 人员: 莉光哈哈哈


import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.XPATH, value='//*[@id="topBooks1"]/dd[1]/a[1]')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="topBooks1"]/dd[1]/a[1]').click()
    time.sleep(3)

    driver.find_element(by=By.XPATH, value='//*[@id="optBtn"]/a')
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="optBtn"]/a').click()
    time.sleep(3)
