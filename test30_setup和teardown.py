# 时间：2023/6/13 18:08
# 人员: 莉光哈哈哈

import pytest


def setup_module():
    print("这是setup_module方法")


def teardown_module():
    print("这是teardown_module方法")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test_login():
    print("这是一个外部的方法")


class TestDemo:
    @classmethod
    def setup_class(cls):
        print("setup_class")

    @classmethod
    def setup_method(cls):
        print("setup_method")

    def setup(self):
        print("setup")

    def teardown_class(self):
        print("teardown_class")

    def teardown_method(self):
        print("teardown_method")

    def teardown(self):
        print("teardown")

    def test_one(self):
        print("开始执行 test_one 方法")
        x = "this"
        assert "h" in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = "hello"
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = "hello"
        b = 'hello world"'
        assert a in b


if __name__ == "__main__":
    pytest.main("-v -s")
