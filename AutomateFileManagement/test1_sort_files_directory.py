# @time     ：2024/7/25 10:42
# @author   : 莉光哈哈哈
# @file     : test1_sort_files_directory.py
# @software : PyCharm
'''
自动化文件管理
'''
'''
1.排序目录中的文件-----根据文件扩展名对目录中的文件进行排序
'''
import os
from shutil import move


def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))


'''
2.删除空文件夹-----脚本用于在指定目录中搜索和删除空文件夹，维护干净整洁的文件夹结构
'''
import os


def remove_empty_folders(directory_path):
    for root, dirs, files in os.walk(directory_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)


'''
3.批量重命名文件-----脚本允许同时批量重命名目录中的多个文件，以旧名称和新名称作为输入，并将所有匹配的文件中的旧名称替换为新名称。
'''
import os


def rename_files(directory_path, old_name, new_name):
    for filename in os.listdir(directory_path):
        if old_name in filename:
            new_filename = filename.replace(old_name, new_name)
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
