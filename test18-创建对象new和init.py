# 时间：2023/6/5 16:46
# 人员: 莉光哈哈哈
class Person(object):

    def __new__(cls, *args, **kwargs):
        print("__new__被调用执行了，cls的id值为{0}".format(id(cls)))
        obj=super().__new__(cls)
        print("创建的对象的id为：{0}".format(id(obj)))
        return obj

    def __init__(self,name,age):
        print("__init__被调用执行了，self的id值为{0}".format(id(self)))
        self.name=name
        self.age=age

print("object这个类对象的id为：{0}".format(id(object)))
print("Person这个类对象的id为：{0}".format(id(Person)))

#创建Person类的实例对象
p=Person("张三",30)
print("p这个Person类的实例对象的id为：{0}".format(id(p)))