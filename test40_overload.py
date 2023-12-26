# @time     ：2023/11/27 15:25
# @author   : 莉光哈哈哈
# @file     : test40_overload.py
# @software : PyCharm
# 转发机制实现重载
from functools import singledispatch


@singledispatch
def function(obj):
    print("%r" % (obj))


@function.register(int)
def function_int(obj):
    print("Integer: %d" % (obj))


@function.register(str)
def function_str(obj):
    print("String: %s" % (obj))


@function.register(list)
def function_list(obj):
    print("List: %r" % (obj))


if __name__ == '__main__':
    function(1)
    function('hello')
    function(range(3))
    function(object)

