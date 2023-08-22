# 时间：2023/6/17 11:27
# 人员: 莉光哈哈哈
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@pytest.mark.parametrize("data", ["云上夕轮", "遇见世界和你"])
def test_Demo(data):
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.CLASS_NAME, value="s_int").send_keys(data)
    time.sleep(3)
    driver.find_element(by=By.CLASS_NAME, value="search_btn").click()
    time.sleep(3)

    assert driver.title == "全部作品_读书屋"


