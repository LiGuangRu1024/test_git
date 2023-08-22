# 时间：2023/6/1 11:28
# 人员: 莉光哈哈哈
'''a=1
while a<10:
    print(a)
    a+=1'''



'''a=0
sum=0
while a<=4:
    sum+=a
    a+=1
print(sum)'''


'''sum=0
for i in range(0,102,2):
    sum+=i
print(sum)'''


'''
import math
def power(x):
    return x*x
print(power(3))'''

import math
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5,2))

