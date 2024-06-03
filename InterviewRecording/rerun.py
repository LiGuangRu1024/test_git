# @time     ：2024/6/3 14:12
# @author   : 莉光哈哈哈
# @file     : rerun.py
# @software : PyCharm
import unittest
from unittestreport import rerun

'''
单个用例重运行
-----自己去标记失败需要重运行的测试用例
'''


class TestClass01(unittest.TestCase):
    @rerun(count=4, interval=2)
    def test_case_01(self):
        a = 100
        b = 99
        assert a == b

    def test_case_02(self):
        a = 100
        b = 100
        assert a == b

    def test_case_03(self):
        a = 100
        b = 101
        assert a == b


'''
全部用例失败重跑机制
-------针对运行的所有的测试用例，只要运行失败的用例就会重运行该用例
'''


class TestClass02(unittest.TestCase):
    def test_case_04(self):
        a = 100
        b = 99
        assert a == b

    def test_case_05(self):
        a = 100
        b = 101
        assert a == b
