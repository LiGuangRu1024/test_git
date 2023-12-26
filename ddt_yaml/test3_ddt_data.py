# @time     ：2023/11/22 14:19
# @author   : 莉光哈哈哈
# @file     : test3_ddt_data.py
# @software : PyCharm

from ddt import ddt, data, unpack, file_data
import unittest

list01 = ['胡歌', '刘亦菲', '彭于晏']
list02 = ['张颂文', '刘德华']

data_dict = {
    'name': '刘诗诗',
    'gender': '女',
    'school': '北京电影学院',
    'hobby': '表演'
}
file_path = 'data/testYaml.yaml'


@ddt
class DDT_yaml(unittest.TestCase):
    @data(list01)  # 传递数据，数据未分离
    def test_01(self, value01):
        print('list01', value01)
        print("-----------------------------------------------")

    @unpack  # 拆分数据，数据分离
    @data(list02)
    def test_02(self, value02, vlu3):
        print('list02', value02)
        print('list02', vlu3)
        print("------------------------------------------------")

    @unpack  # 拆分数据，数据分离
    @data(data_dict)
    # 注意，这里的参数名要和数据文件里参数名(键名)一致
    def test_03(self, name, gender, school, hobby):
        print('data_dict', name)
        print('data_dict', gender)
        print('data_dict', school, hobby)
        print("------------------------------------------------")

    @unpack
    @file_data(file_path)  # 获取指定文件（yaml或json）内部数据
    def test_file_path(self, name, gender, school, hobby):
        print('test_file_path', name)
        print('test_file_path', gender)
        print('test_file_path', school, hobby)


if __name__ == '__main__':
    unittest.main()
    # pass
