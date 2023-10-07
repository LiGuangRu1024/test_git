# 时间：2023/9/27 10:25
# 人员: 莉光哈哈哈
import pytest
from hamcrest import *


class TestAssertHamcrest:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_assert(self):
        a = 10
        b = 20
        assert a < b

    def test_hamcrest(self):
        assert_that(10, equal_to(9), '这是一个提示')
        assert_that(12.0, close_to(10.0, 2.00))
        assert_that("contains some string", contains_string("string"))
