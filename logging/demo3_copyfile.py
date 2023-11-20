# @time     ：2023/11/20 16:45
# @author   : 莉光哈哈哈
# @file     : demo3_copyfile.py
# @software : PyCharm
# 文件的复制
from shutil import copy
# copy的目标可以是一个文件夹也可以是一个文件
from shutil import copyfile
# copyfile的目标只能是一个文件
import os

# 获取来源文件路径
path = os.path.join(os.getcwd(), 'demo2.txt')
# 获取目标路径
target = os.path.join(os.getcwd(), 'images')
# 将目标文件复制到相对路径下
copy(path, target)
