# @time     ：2024/7/26 10:09
# @author   : 莉光哈哈哈
# @file     : test6_interact_database.py
# @software : PyCharm
'''
1.连接数据库
'''
import sqlite3


def connect_to_database(database_path):
    connection = sqlite3.connect(database_path)
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


'''
2.执行SQL查询
'''
import sqlite3


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result


'''
3.数据备份和恢复
'''
import shutil


def backup_database(database_path, backup_directory):
    shutil.copy(database_path, backup_directory)


def restore_database(backup_path, database_directory):
    shutil.copy(backup_path, database_directory)
