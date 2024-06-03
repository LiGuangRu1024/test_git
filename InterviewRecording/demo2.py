# @time     ：2023/12/27 17:06
# @author   : 莉光哈哈哈
# @file     : demo2.py
# @software : PyCharm
'''
匹配出163 的邮箱地址，且@符号之前有4到20 位，例如 hello@163.com
'''
import re


def main(mail_addr):
    ret = re.match(r"[a-zA-Z0-9]{4,20}@(163|126)\.com$", mail_addr)
    print(ret.group())


if __name__ == '__main__':
    mail_addr = input("请输入一个要匹配的邮箱地址：")
    main(mail_addr)

