# @time     ：2023/11/27 14:40
# @author   : 莉光哈哈哈
# @file     : test6_dict.py
# @software : PyCharm
# 字典合并
dict1 = {'a': 10, 'b': 8}
dict2 = {'c': 6, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)

print("---------------------------------------")


def merge(dict4, dict5):
    return (dict5.update(dict4))


dict4 = {'lucky': 0}
dict5 = {'emo': '777'}
print(merge(dict4, dict5))
print(dict5)
