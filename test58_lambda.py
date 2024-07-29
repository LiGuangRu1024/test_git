# @time     ：2024/7/24 14:56
# @author   : 莉光哈哈哈
# @file     : test58_lambda.py
# @software : PyCharm
'''
lambda函数是一种简洁的方式定义单行的小型匿名函数。通常用于需要一个函数作为参数的情况
'''

'''
1.计算两个数的和
'''
add = lambda x, y: x + y
result = add(5, 3)
print(result)

'''
2.找出列表中的偶数
'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

'''
3.对列表元素排序
'''
data = [('apple', 2), ('orange', 1), ('banana', 3)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

'''
4.计算列表元素的平方
'''
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

'''
5.找出最大值
'''
max_value = max([1, 2, 3, 4], key=lambda x: x)
print(max_value)

'''
6.计算平均值
'''
average = lambda lst: sum(lst) / len(lst) if lst else 0
numbers = [1, 2, 3, 4, 5]
print(average(numbers))

'''
7.字符串拼接
'''
join_strings = lambda *args: ''.join(args)
print(join_strings('Hello', '', 'World'))

'''
8.反转字符串
'''
reverse_string = lambda s: s[::-1]
print(reverse_string('hello'))
