# 时间：2023/6/14 14:33
# 人员: 莉光哈哈哈

import pytest


def test_success():
    # "this test succeeds"
    assert True


def test_failure():
    # "this test fails"
    assert False


def test_skip():
    # "this test is skipped"
    pytest.skip("for a reason!")


def test_broken():
    raise Exception("oops")
