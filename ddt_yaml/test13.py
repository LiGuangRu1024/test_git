# @time     ：2023/12/27 15:29
# @author   : 莉光哈哈哈
# @file     : test13.py
# @software : PyCharm
a = [1, 2, 3, 2, 4]


def even(x):
    return x % 2 == 0


# 列表推导，但创建了一个新的变量
a[:] = [x for x in a if not even(x)]
print(a)
print("-----------------------------------------------------")
a = [2, 2, 2, 1, 3, 4]


def even(x):
    return x % 2 == 0


for i in a[:]:
    if even(i):
        a.remove(i)
print(a)
print("--------------------------------------------------------")
a = [1, 2, 2, 3, 4]


def even(x):
    return x % 2 == 0


for i in a:
    if even(i):
        a.remove(i)
print(a)
