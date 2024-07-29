# @time     ：2024/7/25 15:57
# @author   : 莉光哈哈哈
# @file     : test5_automate_spreadsheets.py
# @software : PyCharm
'''
自动化读取excel电子表格
'''
'''
1.读写excel
'''
import pandas as pd


def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df


def write_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)


'''
2.数据分析和可视化
'''
import pandas as pd
import matplotlib.pyplot as plt


def analyze_and_visualize_data(data):
    # 此处编写数据分析和可视化的代码
    pass


'''
3.合并多个表格
'''

import pandas as pd


def merge_sheets(file_path, output_file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.DataFrame()

    for sheet_name in xls.sheet_names:
        sheet_df = pd.read_excel(xls, sheet_name)
        df = df.append(sheet_df)

    df.to_excel(output_file_path, index=False)
