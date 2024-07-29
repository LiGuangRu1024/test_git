# @time     ：2024/7/17 10:50
# @author   : 莉光哈哈哈
# @file     : test50_data_cleaning.py
# @software : PyCharm
'''
1.处理缺失值
df_cleaned=df.dropna()#删除任何包含缺失值的行
df_cleaned=df.fillna(df.mean())#用每列的均值填充缺失值
'''

'''
2. 数据类型不一致
错误表现：数据集中同一列的数据类型不一致，比如混合了字符串和数值。

解决策略：

强制转换数据类型：使用astype()函数。
df['column'] = df['column'].astype(float)  # 将列转换为浮点数类型
3. 异常值处理
错误表现：数据集中存在异常值，可能由于测量误差或其他原因导致。

解决策略：

识别异常值：可以使用IQR（四分位距）方法或Z-score方法。
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
替换或删除异常值：根据具体情况决定是替换异常值还是删除相关行。
4. 重复数据
错误表现：数据集中存在重复记录，可能导致统计结果失真。

解决策略：

检测并删除重复项：使用duplicated()和drop_duplicates()函数。
df_cleaned = df.drop_duplicates()  # 删除所有重复的行
5. 数据格式不统一
错误表现：同一列数据格式不一致，如日期格式、货币单位等。

解决策略：

统一数据格式：使用str.replace()、str.extract()等方法统一格式。

df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')  # 统一日期格式

'''