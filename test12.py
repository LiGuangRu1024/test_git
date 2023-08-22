# 时间：2023/6/5 10:24
# 人员: 莉光哈哈哈12
try:
    a=int(input("输入数字一："))
    b=int(input("输入数字二:"))
    result=a/b
except BaseException as e:
    print("出错了")
else:
    print("计算结果为：",result)
finally:
    print("谢谢使用")

print("----------------------")
import traceback
try:
    print("-------------")
    print(1/0)
except:
    traceback.print_exc()