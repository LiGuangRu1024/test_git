# @time     ：2023/12/21 10:19
# @author   : 莉光哈哈哈
# @file     : test12_container.py
# @software : PyCharm
'''
Python 中的 collections 模块实现了专门的容器数据类型， 为 Python 的通用内置容器: dict、list、set 和 tuple 提供了替代方案。
主要包括以下工具：
1、namedtuple: 创建 具有命名字段的 tuple 子类
2、OrderedDict: 创建 能够记住添加项目的顺序的 dict 子类
3、Counter: 创建 计数器的 dict 子类
4、defaultdict : 创建 存在默认值的 dict 子类
5、deque : 创建 双端队列的 list 子类
'''
# # counter是一个字典。 存储元素字典的键，其计数值作为字典的值。
# from collections import Counter
#
# a = "aaaaabbbbbccdde"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
#
# my_list = [0, 1, 2, 1, 0, 3, 5, 3, 4, 2, 4]
# my_counter = Counter(my_list)
# print(my_counter)
# # 出现次数最多的元素
# print(my_counter.most_common(1))
# print(my_counter.most_common(3))
# print(list(my_counter.elements()))

#
# # namedtuple 命名元组
# from collections import namedtuple
#
# # 创建一个具有类名为字符串和字段为字符串的nametuple
# # 字段必须用逗号或者空格分隔在给定的字符串中
# Point = namedtuple('Point', 'x,y')  # 创建一个元组的子类：Point。它的类名为 Point，它的字段为 x 和 y。
#
# pt = Point(1, -4)
# print(pt)
# print(pt._fields)
# print(type(pt))
# print(pt.x, pt.y)
#
# Person = namedtuple('People', 'name,age')
# friend = Person(name='Tom', age=30)
# print(friend.name, friend.age)


# # defaultdict带默认值字典
# '''
# defaultdict 是一个容器，它和普通的 dict 容器相似，但它只有在键不存在时才会设置默认值。 如果你不使用 defaultdict，你需要检查键是否存在，如果不存在，就设置它为你想要的值。
# '''
# from collections import defaultdict
#
# # 初始化为默认整数值，即0
# d = defaultdict(int)
# d['yellow'] = 1
# d['blue'] = 2
# print(d.items())
# print(d['green'])
#
# # 初始化为默认列表值，即空列表
# d = defaultdict(list)
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
# for k, v in s:
#     d[k].append(v)
# print(d.items())
# print(d['green'])

# deque双端队列
'''
deque是一个双端队列， 它可以用来在两端添加或删除元素。 deque 支持线程安全，内存效率高的在两端添加或删除元素，其执行时间为 O(1)。 deque 是一个更常用的栈和队列的衍生，其输入和输出只能在一端。
'''
from collections import deque

d = deque()
# append():将元素添加到右端
d.append('a')
d.append('d')
print(d)
# pop()，从右端删除并返回一个元素
print(d.pop())
print(d)
# popleft()从左端删除并返回一个元素
print(d.popleft())
print(d)
# clear()：清空deque
d.clear()
print(d)
d = deque(['a', 'b', 'c', 'd'])
# 在右端或左端添加一个序列
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j'])
print(d)
# count(x)：返回x在deque中的个数
print(d.count('h'))
# 将deque向右旋转一位
d.rotate(1)
print(d)
# 将deque向左旋转两位
d.rotate(-2)
print(d)
