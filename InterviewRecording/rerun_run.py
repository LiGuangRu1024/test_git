# @time     ：2024/6/3 14:17
# @author   : 莉光哈哈哈
# @file     : rerun_run.py
# @software : PyCharm
import unittest
from unittestreport import TestRunner
from rerun import TestClass01
from rerun import TestClass02

# 加载测试套件
suite01 = unittest.defaultTestLoader.loadTestsFromTestCase(TestClass01)
suite02 = unittest.defaultTestLoader.loadTestsFromTestCase(TestClass02)

# 执行测试用例
runner = TestRunner(suite=suite01)
runner.run()


# 创建执行对象
runner = TestRunner(suite=suite02)
# 执行测试用例，失败重运行设置为3次，间隔时间为2秒
runner.rerun_run(count=3, interval=2)
