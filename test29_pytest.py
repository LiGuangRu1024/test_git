# 时间：2023/6/13 14:55
# 人员: 莉光哈哈哈
import pytest


# def func(x):
#     return x + 1
# def test_answer():
#     assert func(3) == 5


class TestDemo():
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
    # pytest.main()
    # pytest.main("-v -x TestDemo")
    pytest.main(["-v", "-s", "TestDemo"])
