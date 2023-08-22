# 时间：2023/6/14 15:45
# 人员: 莉光哈哈哈

import pytest
import allure


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段html的body块</body>", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file(r"D:\喜格\pycharm\My_PythonProject\Test\images\three.png",
                       attachment_type=allure.attachment_type.PNG)
