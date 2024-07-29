# @time     ：2024/7/25 14:43
# @author   : 莉光哈哈哈
# @file     : test3_text_processing_manipulation.py
# @software : PyCharm
'''
文本处理和操作
'''

'''
1.统计文本文件中的单词数
'''


def count_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        word_count = len(text.split())
    return word_count


'''
2.查找和替换文本
'''


def find_replace(file_path, search_text, replace_text):
    with open(file_path, 'r') as f:
        text = f.read()
        modified_text = text.replace(search_text, replace_text)

    with open(file_path, 'w') as f:
        f.write(modified_text)


'''
3.生成随机文本
'''
import random
import string


def generate_random_text(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    random_text = ''.join(random.choice(letters) for i in range(length))
    return random_text



