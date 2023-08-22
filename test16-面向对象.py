# 时间：2023/6/5 14:42
# 人员: 莉光哈哈哈
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print("汽车已启动")

car=Car("宝马")
car.start()
print(car.brand)


print("-------------------封装--定义私有类-----------------------")
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)
stu=Student("张三",20)
stu.show()

#在类外面使用name和age
print(stu.name)
"print(stu.__age)"
"print(dir(stu))"
print(stu._Student__age)

print("--------------------继承：Python支持多继承---------------------------------")
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex
class Teacher(Person):
    def __init__(self,name,age,teacheryear):
        super().__init__(name,age)
        self.teacheryear=teacheryear
stu=Student("张三",20,"女")
teacher=Teacher("李四",50,9)
stu.info()
teacher.info()

print("------------------方法重写---------------------------------")
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex
    def info(self):
        super().info()
        print("性别为：",self.sex)


class Teacher(Person):
    def __init__(self,name,age,teacheryear):
        super().__init__(name,age)
        self.teacheryear=teacheryear
    def info(self):
        super().info()
        print("教龄为：",self.teacheryear)


stu = Student("张三", 20, "女")
teacher = Teacher("李四", 50, 9)
stu.info()
teacher.info()

print("------------------多态：在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象的方法---------------------------------")
class Animal(object):
    def eat(self):
        print("动物要吃东西")
class Dog(Animal):
    def eat(self):
        print("狗爱吃肉骨头")
class Cat(Animal):
    def eat(self):
        print("猫咪爱吃鱼")
class Person(object):
    def eat(self):
        print("人爱吃任何东西")
#定义一个函数
def fun(obj):
    obj.eat()
#调用函数
fun(Dog())
fun(Cat())
fun(Animal())
fun(Person())
