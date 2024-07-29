# @time     ：2024/7/24 11:07
# @author   : 莉光哈哈哈
# @file     : test57_log_chart_display.py
# @software : PyCharm
'''
1.读取和解析日志文件：使用python的内置函数或第三方库如pandas来读取并解析日志文件
2.数据清洗与预处理：将读取的数据转换成可以用于绘图的格式，比如DataFrame
3.使用可视化库：利用matplotlib、seaborn、plotly等库来绘制图表
'''

import pandas as pd
import matplotlib.pyplot as plt

# 读取日志文件
log_data = pd.read_csv('path_to_your_log_file.log')

# 假设日志文件中有以下列：'tunestamp','value'
# 将时间戳转化为datetime对象
log_data['timestamp'] = pd.to_datetime(log_data['timestamp'])

# 按照时间排序数据
log_data = log_data.sort_values('timestamp')

# 使用matplotlib绘制图表
plt.figure(figsize=(10, 5))
plt.plot(log_data['timestamp'], log_data['value'])
plt.title('Value Over Time')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)
plt.show()

'''
若日志格式不是csv格式，而是传统的文本日志，需要使用正则表达式或者自定义函数来解析每一行
'''
import re

# 正则表达式来匹配日志行中的字段
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}),\s+(\w+),\s+(.*)'

# 解析日志文件
parsed_logs = []
with open('path_to_your_log_file.log', 'r') as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            timestamp, level, message = match.groups()
            parsed_logs.append({'timestamp': timestamp, 'level': level, 'message': message})

# 转换为DataFrame
df = pd.DataFrame(parsed_logs)

# 后续的分析和绘图步骤与上面相同
