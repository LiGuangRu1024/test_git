# @time     ：2024/7/22 10:10
# @author   : 莉光哈哈哈
# @file     : test54_image_recognition.py
# @software : PyCharm

'''

1pip install opencv-python-headless scikit-learn numpy

'''

'''
读取和预处理图像----如灰度化、缩放和归一化
'''
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 加载数据集
def load_mnist():
    # 这里需要自己下载MNIST数据集并加载，或者使用Keras加载
    pass


(X_train, y_train), (X_test, y_test) = load_mnist()

# 预处理
X_train = X_train.reshape(-1, 28 * 28) / 255.0
X_test = X_test.reshape(-1, 28 * 28) / 255.0

'''
模拟训练----使用scikit-learn中的Logistic Regression作为分类器进行训练
'''
# 训练模型
model = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=1000)
model.fit(X_train, y_train)

'''
模型评估----使用测试集评估模型的准确性
'''
# 评估模型
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

'''
图像识别----使用模型识别一张图片中的数字
'''


def recogize_digit(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.reshape(1, -1) / 255.0
    prediction = model.predict(img)
    return prediction[0]

#测试识别
image_path='path_to_your_image.jpg'
print("Predicted digit:",recogize_digit(image_path))