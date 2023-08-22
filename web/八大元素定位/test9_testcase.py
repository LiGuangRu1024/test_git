# 时间：2023/6/19 16:44
# 人员: 莉光哈哈哈


import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_Demo():
    driver = webdriver.Chrome()
    driver.get("https://test-medical.wenetwork.cn:442/#/login")
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[2]/div/div/input').send_keys("100021")
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[3]/div/div/input').send_keys("16688889999")
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[4]/div/div/input').send_keys("123456")
    time.sleep(1)
    driver.find_element(by=By.TAG_NAME, value='button').click()
    time.sleep(3)


