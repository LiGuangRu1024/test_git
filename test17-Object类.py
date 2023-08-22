# 时间：2023/6/5 15:36
# 人员: 莉光哈哈哈
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "我的名字是{0},今年{1}岁".format(self.name,self.age)
stu=Student("张三",80)
print(dir(stu))
print(stu)