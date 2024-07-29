# @time     ：2024/7/17 11:47
# @author   : 莉光哈哈哈
# @file     : test52_progress_bar.py
# @software : PyCharm
'''
1.tqdm------tqdm是一个快速、可扩展的进度条库，它可以在长循环或者迭代器上添加进度提示
'''
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.1)  # 模拟耗时操作

'''
2.alive_progress----alive_progress提供了动态的进度条效果，特别适合长时间运行的任务，它可以自动调整进度条的长度以适应终端窗口大小
'''
# pip install alive-progress

from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    for i in range(100):
        time.sleep(0.1)  # 模拟耗时操作
        bar()

'''
3.progress-----progress库提供了创建进度条的简单方法
'''
from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # 模拟处理
    time.sleep(1)
    bar.next()
bar.finish()

'''
4.自定义简单进度条-----如果不希望使用额外的库，可以手动实现一个简单的文本进度条
'''


def simple_progress_bar(total, width=50):
    for i in range(total + 1):
        progress = i / total
        hashes = '#' * int(progress * width)
        spaces = '' * (width - len(hashes))
        print(f'\rProgress:[{hashes}{spaces}] {int(progress * 100)}%', end="")
        time.sleep(0.1)  # 模拟耗时操作


simple_progress_bar(100)
