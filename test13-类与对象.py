# 时间：2023/6/5 11:30
# 人员: 莉光哈哈哈
class Student:
    pass


print(id(Student))
print(type(Student))
print(Student)

print("---------------------------------------------")


class Student:
    # 类属性
    navtive_pace = "吉林"

    # 初始化方法
    def __init__(self, name, age):  # name，age为实例属性
        self.name = name
        self.age = age

    # 实例方法
    def info(self):
        print(self.name, self.age)

    # 类方法
    @classmethod
    def cm(cls):
        print("类方法")

    # 静态方法
    @staticmethod
    def sm():
        print("静态方法")


# 创建Student类的对象
stu = Student("张三", 20)
print(id(stu))
print(type(stu))
print(stu)

# 实例方法
stu.info()
