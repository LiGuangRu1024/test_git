# 时间：2023/6/5 17:01
# 人员: 莉光哈哈哈


#python拷贝一般是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，所以源对象与拷贝对象会引用同一个子对象
#深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
print("-------------变量的赋值操作：只是形成两个变量，实际上还是指向同一个对象--------------------")
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

print("-----------------类的浅拷贝----------------------------")
disk=Disk()  #创建硬盘类的对象
computer1=Computer(cpu1,disk)   #创建计算机类的对象

import copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)


print("-----------------类的深拷贝----------------------------")
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)

