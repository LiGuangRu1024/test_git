# 时间：2023/5/29 16:02
# 人员: 莉光哈哈哈
print(chr(0b100111001011000))
print(ord("乘"))
print("--------------------------------------------")


#保留字
import keyword
print(keyword.kwlist)
print("--------------------------------------------")


name="张亚茹"
print(name)
print("标识",id(name))
print("类型",type(name))
print("值",name)
print("--------------------------------------------")


#整数可以表示为二进制，十进制，八进制，十六进制
print("十进制",118)
print("二进制",0b10101111)#二进制以0b开头
print("八进制",0o176)#八进制以0o开头
print("十六进制",0x1EAF)#十六进制以0x开头
print("--------------------------------------------")



#使用浮点数进行计算时，可能会出现小数位数不确定的情况。解决方案：导入模块decimal
from decimal import  Decimal
print(Decimal("1.1")+Decimal("2.2"))
print("--------------------------------------------")



#布尔值可以转化为整数    True为1，False为0
print(True+1)
print(False+1)
print("--------------------------------------------")



name="张小小"
age=18
print(type(name),type(age)) #说明name与age的数据类型不相同#
#print( '我叫'+name+'今年'+age+'岁') #当将str类型与int类型进行连接时，报错，解决方案，类型转换
print( '我叫'+name+'今年'+str(age)+'岁')#将int类型通过str()函数转成了str类型
print("--------------------------------------------")



print('---str()将其它类型转成str类型---')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))
