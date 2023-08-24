# 时间：2023/8/24 18:14
# 人员: 莉光哈哈哈
# 调整用例执行顺序
import pytest


def test_03():
    print("test_03")


def test_04():
    print("test_04")


class TestA(object):
    def test_05(self):
        print("test_05")

    @pytest.mark.last
    def test_06(self):
        print("test_06")


class TestB(object):
    @pytest.mark.run(order=1)
    def test_01(self):
        print("test_01")

    def test_02(self):
        print("test_02")
