# @time     ：2023/12/12 15:09
# @author   : 莉光哈哈哈
# @file     : test42_上下文管理器.py
# @software : PyCharm
# 自定义上下文管理器
# class ManagedFile:
#     def __init__(self, filename):
#         print("初始化类", filename)
#         self.filename = filename
#
#     def __enter__(self):
#         print("》》》进入上下文管理《《《")
#         self.file = open(self.filename, "w")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#         print("执行：", exc_type, exc_val)
#         if exc_type is not None:
#             print("管理器内，处理异常")
#         print("《《《退出上下文管理》》》")
#         return True
#
#
# with ManagedFile("notes.txt") as f:
#     print("一些操作。。。。。。。")
#     f.write("写入内容。。。。。。。")
# print("继续。。。。。。。")
#
# # 抛出异常，文件仍然关闭
# with ManagedFile("notes.txt") as f:
#     print("一些操作。。。。。。。")
#     f.write("写入内容。。。。。。。")
#     f.do_someting()  # 此方法会抛出异常
# print("继续。。。。。。。")


from contextlib import contextmanager


# 实现上下文管理器为生成器
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        print("》》》进入上下文管理器《《《")
        yield f
    finally:
        print("《《《退出上下文管理》》》")
        f.close()


with open_managed_file('notes.txt') as f:
    print("一些操作。。。。。。。")
    f.write("写入内容。。。。。。。")
