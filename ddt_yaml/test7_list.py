# @time     ：2023/11/27 15:57
# @author   : 莉光哈哈哈
# @file     : test7_list.py
# @software : PyCharm
# 统计列表中每个元素出现的次数
# from collections import Counter
#
# lists=[1,2,5,1,1,5,6,3,3,2,2,4,8]
#
# arr=Counter(lists)
#
# print(arr)


list1 = [1, 5, 5, 2, 2, 2, 1, 3]


def all_list(list1):
    result = {}
    for i in set(list1):
        result[i] = list1.count(i)
    return result


print(all_list(list1))


numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers)