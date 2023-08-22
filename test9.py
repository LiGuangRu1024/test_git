# 时间：2023/6/3 15:50
# 人员: 莉光哈哈哈
lst=[10,5,80,30,100,40]
lst.sort()
print("排序后的列表",lst)
print("------------------")

lst.sort(reverse=True)
print(lst)
print("------------------")

lst.sort(reverse=False)
print(lst)


print("--------------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象-------------------------")
lst=[90,76,20,100,7,89,10]
new_lst=sorted(lst)
print(lst)
print(new_lst)

print("--------------生成列表的公式------------------------------------------------------------")
lst=[i*i for i in range(1,10)]
print(lst)

print("--------------生成集合的公式------------------------------------------------------------")
s={i*i for i in range(1,10)}
print(s)
