# 时间：2023/8/24 16:13
# 人员: 莉光哈哈哈
import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，打开百度首页")

    yield

    print("执行teardown")
    print("关闭浏览器")


def test_case0():
    print("用例case0")


def test_case1(open):
    print("用例case1")


def test_case2(open):
    print("用例case2")
