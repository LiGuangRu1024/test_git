# @time     ：2024/8/15 16:20
# @author   : 莉光哈哈哈
# @file     : test62_data_merging.py
# @software : PyCharm
'''
数据合并与聚合
'''
import pandas as pd

# 创建示例数据
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

df2 = pd.DataFrame({
    'C': ['C0', 'C1'],
    'D': ['D0', 'D1'],
    'key': ['K0', 'K1']
})

# 数据合并
merged_inner = pd.merge(df1, df2, on='key')
merged_outer = pd.merge(df1, df2, on='key', how='outer')
merged_left = pd.merge(df1, df2, on='key', how='left')
merged_right = pd.merge(df1, df2, on='key', how='right')

# 显示合并结果
print("Inner Join:")
print(merged_inner)
print("\nOuter Join:")
print(merged_outer)
print("\nLeft Join:")
print(merged_left)
print("\nRight Join:")
print(merged_right)

# 数据聚合
grouped = df1.groupby('key')
mean_A = grouped['A'].mean()
describe_AB = grouped[['A', 'B']].describe()

# 显示聚合结果
print("\nMean of Column A by Group:")
print(mean_A)
print("\nDescriptive Statistics by Group:")
print(describe_AB)

# 使用 agg 方法
agg_result = df1.groupby('key').agg({'A': ['mean', 'sum'], 'B': 'count'})
print("\nAggregation Result:")
print(agg_result)

# 使用 apply 方法
length_of_A = df1['A'].str.len().mean()
print("\nAverage Length of Column A:")
print(length_of_A)

