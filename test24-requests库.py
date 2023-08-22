# 时间：2023/6/10 14:02
# 人员: 莉光哈哈哈


import requests

# res = requests.get("http://www.baidu.com")
# print(res)

res=requests.post("http://httpbin.org/post",data={"key":"value"})
print(res.text)