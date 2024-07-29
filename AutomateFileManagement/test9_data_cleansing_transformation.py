# @time     ：2024/7/26 14:39
# @author   : 莉光哈哈哈
# @file     : test9_data_cleansing_transformation.py
# @software : PyCharm
'''
1.从数据中删除重复项----确保数据完整性和提高数据分析
'''
import pandas as pd


def remove_duplicates(data_frame):
    cleaned_data = data_frame.drop_duplicates()
    return cleaned_data


'''
2.数据规范化-----将数据集中的值缩放到0到1范围内
'''
import pandas as pd


def normalize_data(data_frame):
    normalized_data = (data_frame - data_frame.min()) / (data_frame.max() - data_frame.min())
    return normalized_data


'''
3.处理缺失值-----使用向前填充方法用前一个非缺失值填充缺失值
'''
import pandas as pd

def handle_missing_values(data_frame):
    filled_data=data_frame.fillna(method='ffill')
    return filled_data
