# 时间：2023/6/13 18:44
# 人员: 莉光哈哈哈
import pytest





def test_case1(login):
    print("test_case01")
    pass


def test_case02():
    print("test_case02")
    pass


def test_case03(login):
    print("test_case03")
    pass


if __name__ == "__main__":
    pytest.main("-v -s")
