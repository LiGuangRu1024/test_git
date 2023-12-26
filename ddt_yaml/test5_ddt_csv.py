# @time     ：2023/11/27 14:27
# @author   : 莉光哈哈哈
# @file     : test5_ddt_csv.py
# @software : PyCharm
import csv
import unittest
from ddt import *


def getCsvData():
    value_rows = []
    with open('../data/user.csv', encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows
