# 时间：2023/6/5 11:55
# 人员: 莉光哈哈哈
class Student:
    #类属性
    navtive_pace="吉林"

    #初始化方法
    def __init__(self,name,age):            #name，age为实例属性
        self.name=name
        self.age=age
    #实例方法
    def info(self):
        print(self.name,self.age)

    def eat(self):
        print("学生在吃饭")

    #类方法
    @classmethod
    def cm(cls):
        print("这是类方法")

    #静态方法
    @staticmethod
    def sm():
        print("这是静态方法")

#类属性的使用
print("---------类属性的使用------------------")
print(Student.navtive_pace)
stu1=Student("张三",10)
stu2=Student("李四",20)
print(stu1.navtive_pace)
print(stu2.navtive_pace)

print("----------类方法的使用-------------------------")
Student.cm()

print("----------静态方法的使用-------------------------")
Student.sm()