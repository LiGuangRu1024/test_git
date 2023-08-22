# 时间：2023/6/6 14:37
# 人员: 莉光哈哈哈

#
# import package.module1 as ma  #ma为package.module1这个模块的别名
# print(ma.a)

print("---------------------")

# from package import module2
# from package.module1 import ma



import urllib.request
print(urllib.request.urlopen("http://www.baidu.com").read())

print("------------------------------------------")
print(urllib.request.urlopen("http://www.baidu.com").status)
print("----------------------------------------------")

print(urllib.request.urlopen("http://www.baidu.com").headers)