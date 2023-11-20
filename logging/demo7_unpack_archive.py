# @time     ：2023/11/20 18:02
# @author   : 莉光哈哈哈
# @file     : demo7_unpack_archive.py
# @software : PyCharm
# 文件解压
# 使用方法：unpack_archive(要解压的文件，解压后的路径)


from shutil import unpack_archive
import os

path = os.path.join(os.getcwd(), 'logging')
unpack_archive('logging压缩包.zip', path)
