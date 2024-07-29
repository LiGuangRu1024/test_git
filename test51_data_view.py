# @time     ：2024/7/17 10:57
# @author   : 莉光哈哈哈
# @file     : test51_data_view.py
# @software : PyCharm

'''
1. Matplotlib-----Matplotlib是最基础的绘图库，几乎可以绘制所有类型的静态图像。
'''

import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建图表
plt.plot(x, y, label="First Line")
plt.legend()

# 添加标题和轴标签
plt.title('Simple Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图表
plt.show()

'''
2. Seaborn-----Seaborn是基于Matplotlib的，它提供了更高级的界面用于绘制统计图形。
'''
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成数据
np.random.seed(0)
data = np.random.randn(100, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# 使用Seaborn绘制箱线图
sns.boxplot(data=df)

# 显示图表
plt.show()

'''
3.Plotly-----Plotly可以生成交互式图表，非常适合网页应用
'''
import plotly.graph_objects as go

# 数据
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 创建图表
fig = go.Figure(data=go.Scatter(x=x, y=y))

# 自定义布局
fig.update_layout(title='Interactive Plot', xaxis_title='X Axis', yaxis_title='Y Axis')

# 显示图表
fig.show()

'''
4.Bokeh-----Bokeh是一个用于生成交互式图表的库，特别适合大数据集
'''
from bokeh.plotting import figure, show, output_notebook
from bokeh.io import output_file

# 输出到HTML文件
output_file("line.html")

# 准备数据
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# 创建图表
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label='Temp.', line_width=2)

# 显示图表
show(p)

'''
5. Pandas Visualization-----Pandas自带一些基本的绘图功能，可以直接在DataFrame上调用。
'''
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 创建DataFrame
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])

# 直接在DataFrame上调用plot方法
df.plot(kind='bar')

# 显示图表
plt.show()
