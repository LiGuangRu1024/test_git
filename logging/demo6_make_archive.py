# @time     ：2023/11/20 18:00
# @author   : 莉光哈哈哈
# @file     : demo6_make_archive.py
# @software : PyCharm
# 文件压缩
# make_archive(压缩之后的文件名，压缩后缀，希望压缩的文件或目录)。


from shutil import make_archive
import os

path = os.path.join(os.getcwd(), 'testfile')
make_archive('logging压缩包', 'zip', path)
