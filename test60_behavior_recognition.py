# @time     ：2024/8/15 10:51
# @author   : 莉光哈哈哈
# @file     : test60_behavior_recognition.py
# @software : PyCharm
'''
数据预处理
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 加载数据
data = pd.read_csv("dataset.csv")

# 分割特征和标签
X = data.drop("label", axis=1)
y = data['label']

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_suze=0.2, random_state=42)

# 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 训练模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 评估模型
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy:{accuracy:.2f}")

'''
行为识别
'''
import cv2
import numpy as np

# 加载模型和标准化器
model = LogisticRegression()
model.load("trained_model.pkl")  # 加载训练好的模型
scaler = StandardScaler()
scaler.load("scaler.pkl")  # 加载标准化器

# 初始化摄像头
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # 对图像进行预处理
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (64, 64))  # 假设特征向量大小为64×64

    # 特征提取
    features = resized.flatten().reshape(1, -1)
    features = scaler.transform(features)

    # 使用模型预测
    prediction = model.predict(features)

    # 显示预测结果
    cv2.putText(frame, f"Behavior:{prediction[0]}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Behavior Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理
cap.release()
cv2.destroyAllWindows()
