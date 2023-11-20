# @time     ：2023/11/20 17:57
# @author   : 莉光哈哈哈
# @file     : demo5_remove.py
# @software : PyCharm
# 文件的删除
from os import remove

import os

path = os.path.join(os.getcwd(), 'demo2.txt')
remove(path)
