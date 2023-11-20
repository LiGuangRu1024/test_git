# @time     ：2023/10/13 18:00
# @author   : 莉光哈哈哈
# @file     : demo1.py
# @software : PyCharm
"""
handlers处理器:日志信息 输出到你想要的位置 控制台处理器 文本文件处理器
formatter格式器:处理日志格式 格式比较好看
filter过滤器
    日志级别:
1.debug级别:调试级别 1
2.info级别:正常级别 2
3.warning警告:有问题但不影响程序运行 3
4.error级别:错误的 4
5.critical:严重的 程序崩溃5
"""
import logging

# 设置日志级别，默认级别warning
logging.basicConfig(level=logging.DEBUG)
logging.info('正常')
logging.error('错误')
logging.debug('调试')
logging.warning('警告')
logging.critical('严重')
