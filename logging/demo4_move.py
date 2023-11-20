# @time     ：2023/11/20 17:52
# @author   : 莉光哈哈哈
# @file     : demo4_move.py
# @software : PyCharm
# 文件的裁剪
from shutil import move
# move(来源地址，目标地址)

import os

path = os.path.join(os.getcwd(), 'demo2.txt')
target = os.path.join(os.getcwd(), 'test')
move(path, target)
