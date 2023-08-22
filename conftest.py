# 时间：2023/6/13 18:49
# 人员: 莉光哈哈哈

import pytest


@pytest.fixture()
def login():
    print("这是个登陆方法")


def pytest_configure(config):
    marker_list = ["search", "login"]  # 标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
