# 时间：2023/6/14 9:59
# 人员: 莉光哈哈哈

import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown")
    print("最后关闭浏览器")


def test_search1(open):
    print("test_search1")
    raise NameError
    pass


def test_search2(open):
    print("test_search2")
    pass


def test_search3(open):
    print("test_search3")
    pass


if __name__ == "__main__":
    pytest.main()
