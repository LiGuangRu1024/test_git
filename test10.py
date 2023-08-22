# 时间：2023/6/3 17:00
# 人员: 莉光哈哈哈
dict={"张三":100,"李四":80,"王五":87}
print(dict["张三"])
print(dict.get("张三"))
print('------------------------------------')

keys=dict.keys()
print(list(keys))
print("------------------------------------")

values=dict.values()
print(list(values))
print(values)
print("------------------------------------")

items=dict.items()
print(list(items))   #转换之后的列表元素由元组组成

print("------------字典元素的遍历-------------------------")
for i in dict:
    print(i,dict[i],dict.get(i))

print("---------------内置函数zip()-------------------------------")
items=["zhangsan","lisi","wangwu"]
prices=[90,70,89]
d={items.upper():prices for items,prices in zip(items,prices)}
print(d)