# 时间：2023/6/5 17:27
# 人员: 莉光哈哈哈

def fun():
    pass
def fun2():
    pass

class Student:
    native_place="吉林"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def sm():
        pass
    @classmethod
    def cm(cls):
        pass

a=2
b=4
print(a+b)

print("------------------模块的导入------------------------")
import math
print(id(math))
print(type(math))
print(math)
print(math.pi)

print(dir(math))

print("------------------------------------------------")
from math import pi
print(pi)
print(pow(2,3))
print(math.pow(2,3))



