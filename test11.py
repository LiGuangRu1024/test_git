# 时间：2023/6/3 17:32
# 人员: 莉光哈哈哈
#空列表创建
a1=[]
a2=list()
#空字典创建
b1={}
b2=dict()
#空元组创建
c1=()
c2=tuple()
#空集合创建
d=set()
print(a1,a2,b1,b2,c1,c2,d)

print("----------------------------")
tuple=(10,[89,90],80)
print(tuple[0])
print(tuple[1])
print(tuple[2])
tuple[1].append(100)
print(tuple)

print("-------------元组的遍历--------------------")
tuple=("python","hello",801,192)
for i in tuple:
    print(i)


