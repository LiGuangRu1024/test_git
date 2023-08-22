# 时间：2023/6/14 11:07
# 人员: 莉光哈哈哈

import pytest


@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
    pass


@pytest.mark.search
def test_search2():
    print("test_search2")
    pass


@pytest.mark.search
def test_search3():
    print("test_search3")
    pass


@pytest.mark.login
def test_login1():
    print("test_login1")
    pass


@pytest.mark.login
def test_login2():
    print("test_login2")
    pass


if __name__ == "__main__":
    pytest.main()
