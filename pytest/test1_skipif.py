# 时间：2023/8/24 14:14
# 人员: 莉光哈哈哈
import pytest
import sys

environment = 'android'


@pytest.mark.skipif('environment == "android"', reason='android平台没有这个功能')
def test_cart_1():
    pass


@pytest.mark.skipif(sys.platform == 'mac', reason='不在mac下运行')
@pytest.mark.skipif(sys.version_info < (3, 6), reason='3.6坂本一下不执行，你需要更高版本')
def test_cart_2():
    print("当python版本大于或等于3.6时执行，mac下不执行")
    pass
