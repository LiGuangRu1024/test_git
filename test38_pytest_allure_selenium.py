# 时间：2023/6/14 16:40
# 人员: 莉光哈哈哈

import allure
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", ["allure", "pytest", "unitest"])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element(by=By.ID, value='kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element(by=By.ID, value="su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot(r"D:\喜格\pycharm\My_PythonProject\Test\images\one.png")
        allure.attach.file(r"D:\喜格\pycharm\My_PythonProject\Test\images\one.png",
                           attachment_type=allure.attachment_type.PNG)
    # allure.attach("<head></head><body>首页</body>，Attach with HTML type", allure.attachment_type.HTML)
    with allure.step("关闭浏览器"):
        driver.quit()
