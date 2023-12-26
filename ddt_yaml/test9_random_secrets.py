# @time     ：2023/12/13 10:08
# @author   : 莉光哈哈哈
# @file     : test9_random_secrets.py
# @software : PyCharm
import random

a = random.random()  # 取0到1之间的随机浮点数（0.0 <= a < 1.0）
print(a)

a = random.uniform(1, 10)  # 取1到10之间的随机浮点数（1.0 <= a < 10.0 ）
print(a)

a = random.randint(1, 10)  # 取1到10之间的随机整数（1 <= a <= 10）
print(a)

a = random.randrange(1, 10)  # 取1到10之间的随机整数（1 <= a <= 10）
print(a)

a = random.normalvariate(0, 1)  # 设置平均值为0，标准差为1的正态分布随机数
print(a)

a = random.choice(list('ABCDEFG'))  # 从序列中随机选择一个元素
print(a)

a = random.sample(list('ABCDEFGHIJKLMN'), 3)  # 从序列中随机选择3个元素，不重复
print(a)
print(type(a))

a = random.choices(list('ABCDEFGHIJKLMN'), k=3)  # 从序列中随机选择3个元素，可以重复
print(a)

a = list('ABCDEFG')
random.shuffle(a)  # 打乱序列
print(a)

print("-----------------------------------------------------------------------------------")

