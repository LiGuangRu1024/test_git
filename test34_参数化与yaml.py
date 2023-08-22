# 时间：2023/6/14 14:17
# 人员: 莉光哈哈哈

import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load((open("./env.yml"))))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
        elif "dev" in env:
            print("这是开发环境")
