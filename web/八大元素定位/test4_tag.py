# 时间：2023/6/19 9:55
# 人员: 莉光哈哈哈

'''
find_element_by_tag_name
<> tag html的每个元素都是tag，一个tag往往用来定义一类功能
'''

import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@pytest.mark.parametrize("data", ["云上夕轮", "遇见世界和你"])
def test_Demo(data):
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.TAG_NAME, value="input").send_keys(data)
    time.sleep(3)
    driver.find_element(by=By.TAG_NAME, value="label").click()
    time.sleep(3)

    assert driver.title == "全部作品_读书屋"
