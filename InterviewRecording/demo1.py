# @time     ：2023/12/27 16:56
# @author   : 莉光哈哈哈
# @file     : demo1.py
# @software : PyCharm
'''
求一个整数数组里面两个数之和为 183 的所有整数对。例如:输入数组为[183,0,1,2,-184,367],得到结果为{(183,0),-184,367)}
'''

ls = [183, 0, 1, 2, -184, 367]

num = []

for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        if ls[i] + ls[j] == 183:
            num.append((ls[i], ls[j]))
            sum = set(num)
print(sum)
