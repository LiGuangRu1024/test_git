# 时间：2023/6/19 17:04
# 人员: 莉光哈哈哈

'''
异常：程序执行不下去，中断当前程序并抛出异常
'''

try:
    a = 1
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("出错了")


