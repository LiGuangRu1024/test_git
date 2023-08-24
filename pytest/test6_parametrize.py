# 时间：2023/8/24 17:01
# 人员: 莉光哈哈哈
import pytest
from pytest_assume.plugin import assume


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume_with(x, y):
    print("测试数据x=%s,y=%s" % (x, y))
    with assume: assert x == y
    with assume: assert x + y > 1
    with assume: assert x > 1
    print("测试完成")

