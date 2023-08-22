# 时间：2023/6/5 14:22
# 人员: 莉光哈哈哈
class Student:
    #初始化方法
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(self.name+"在吃饭")

stu1=Student("张三",30)
stu2=Student("李四",40)
print(stu1)
print(stu2)
print("------------为stu2动态绑定其他属性---------------------------")
stu2.gender="女"
print(stu2.name,stu2.age,stu2.gender)


print("------------------------------------------------")
stu1.eat()
stu2.eat()

def show():
    print("定义在类之外的函数")
stu1.show=show
stu1.show()

