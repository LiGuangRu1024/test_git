# @time     ：2023/11/29 10:59
# @author   : 莉光哈哈哈
# @file     : test41_深浅拷贝的具体实现.py
# @software : PyCharm
import copy
print("---------------简单可变类型的深浅拷贝都会产生一个新的空间-------可变类型有:列表，字典")
list1 = [1, 2, 3]
print("list1=", list1, id(list1))

print("---------------------------浅拷贝--------------------")
list2 = copy.copy(list1)
print("list2=", list2, id(list2))
print("-------------------------修改list1-------------")
list1.append(5)
print("list1=", list1, id(list1))
print("list2=", list2, id(list2))
print("---------------------------深拷贝--------------------")
list1 = [1, 2, 3]
print("list1=", list1, id(list1))
list2 = copy.deepcopy(list1)
print("list2=", list2, id(list2))
print("-------------------------修改list2-------------")
list2.append(7)
print("list1=",list1,id(list1))
print("list2=",list2,id(list2))
