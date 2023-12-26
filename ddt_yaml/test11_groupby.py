# @time     ：2023/12/19 16:01
# @author   : 莉光哈哈哈
# @file     : test11_groupby.py
# @software : PyCharm
"""
groupby()函数将一个迭代器切分为多个小迭代器。如果后一个元素的key值等于前一个元素的key 值，会将这两个元素放在同一个分组中；如果与前一个元素的key值不同，则当前分组结束，将当前元素放到新的分组中。

groupby()函数的输出是一系列二元组，每个元组包括一个key值和包含该组元素的迭代器，该迭代器的元素可以通过转换保存为元组，也可以归约为汇总值。这种情况下将不会保留迭代器中的值。
"""
# from itertools import groupby
#
#
# # 用函数作为键
# def smaller_than_3(x):
#     return x < 3
#
#
# group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
# for key, group in group_obj:
#     print(key, list(group))
#
# # 或者使用lamda表达式，例如：单词包含‘i’
# group_obj = groupby(['hi', 'hello', 'cool'], key=lambda x: 'i' in x)
# for key, group in group_obj:
#     print(key, list(group))
#
# # 返回一个字典，键是年龄，值是一个列表，列表中包含名字
# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 26}, {'name': 'Lisa', 'age': 27},
#            {'name': 'Jack', 'age': 39}]
# for key, group in groupby(persons, key=lambda x: x['age']):
#     print(key, list(group))

print("--------------------------------------------------------------------------------------")
"""

python有3个无限迭代，分别为count(),cycle(),repeat()
1、count(start[, step]) 无限计数递增迭代，参数start起始数据，可选参数step为步长
2、cycle(p) 无限循环周期性迭代，参数p，周期性循环p序列的数据
3、repeat(elem [,n]) 重复迭代，对elem重复迭代n次

"""
from itertools import count, cycle, repeat

# count(x)：从x开始，每次增加1
for i in count(16):
    print(i)
    if i >= 13:
        break
# cycle(iterable)：无限循环迭代器
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break
# repeat(x, n)：重复x n次
print("")
for i in repeat('A', 4):
    print(i)
