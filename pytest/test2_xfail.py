# 时间：2023/8/24 14:41
# 人员: 莉光哈哈哈


# condition----条件、reason----原因、raises----引起异常、run----是否执行
import pytest


def valid_config():
    return False


class TestPytest:
    # @pytest.mark.xfail(reason="该功能有bug")
    def test_one(self):
        print("--------start---------")
        pytest.xfail(reason="该功能尚未完成")
        print("test_one方法执行")
        assert 2 == 1

    def test_two(self):
        print("test_two方法执行")
        assert "o" in "love"

    def test_three(self):
        print("test_three方法执行")
        assert 3 - 2 == 1

    def test_function(self):
        if not valid_config():
            pytest.xfail("这是个无效的配置，无法进行后续测试")


if __name__ == "__main__":
    pytest.main()
