# 时间：2023/6/17 11:27
# 人员: 莉光哈哈哈
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


# web UI搜索功能测试流程
# 1、打开浏览器
# 2、输入网址
# 3、找到元素
# 4、输入关键字
# 5、点击搜索
# 6、验证结果   assert断言
@pytest.mark.parametrize("data", ["云上夕轮", "遇见世界和你"])
def test_Demo(data):
    driver = webdriver.Chrome()
    driver.get("http://novel.hctestedu.com/")
    driver.find_element(by=By.ID, value="searchKey").send_keys(data)
    time.sleep(3)
    driver.find_element(by=By.ID, value="btnSearch").click()
    time.sleep(3)

    assert driver.title == "全部作品_读书屋"
