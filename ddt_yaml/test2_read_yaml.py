# @time     ：2023/10/13 15:14
# @author   : 莉光哈哈哈
# @file     : test2_read_yaml.py
# @software : PyCharm
import yaml


def read_yaml():
    file = open('./data/data.yaml', 'r', encoding='utf-8')
    values = yaml.load(stream=file, Loader=yaml.FullLoader)
    for value in values:
        print(value)
