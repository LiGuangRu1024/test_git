# @time     ：2023/10/13 10:22
# @author   : 莉光哈哈哈
# @file     : test1_ddt_yaml.py
# @software : PyCharm

"""
1、DDT:UnitTest下非常好的数据驱动器的搭配。数据驱动测试模块，在unittest中是以装饰器的形式存在
2、DDT的使用：
    通过装饰器形态来实现使用
    2.1、@data装饰器的数据驱动实现：导入相对比较简单的数据内容


"""
import unittest
from ddt import data, unpack, file_data


def read_file():
    values = list()
    file = open('./data/data.txt', 'r', encoding='utf-8')
    for line in file.readline():
        values.append(line)
    return values


@data
class UnitAuto(unittest.TestCase):
    def setUpClass(self) -> None:
        pass

    def tearDownClass(self) -> None:
        pass

    @data(['luckily', 'lha'])
    @unpack
    def test_01(self, a, b):
        print(a, b)

    @data(read_file())
    def test_02(self, a):
        # print(a + '以及' + b)
        print(a)

    @file_data('./data/data.yaml')
    def test_03(self, name, age):
        print(name, age)


if __name__ == '__main__':
    unittest.main()
