# @time     ：2024/8/9 16:01
# @author   : 莉光哈哈哈
# @file     : auto_reply_message.py
# @software : PyCharm
'''
pip install pyautogui
pip install opencv-python
'''

import pyautogui
import cv2
import time
import pyperclip


# 从屏幕screen中找到source的位置坐标（找到微信搜索框的位置）
def findImg():
    # 注意：必须打开微信聊天框
    im = pyautogui.screenshot()
    im.save("screen.png")
    screen = cv2.imread("./screen.png")
    joinMeeting = cv2.imread("./screen.png")

    # 微信聊天框与搜索框截图比较，获取相似点
    result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
    pos_start = cv2.minMaxLoc(result)[3]  # 获取最相似点相似坐标

    # 定位到点击图片中的中间位置
    x = int(pos_start[0]) + int(joinMeeting.shape[1] / 2)
    y = int(pos_start[1]) + int(joinMeeting.shape[0] / 2)

    return x, y


# 向搜索框中输入要查找的好友的名字：name--好友名称，x,y搜索框位置
def send_name_to_search(x, y, name):
    # 点击搜索框，光标闪烁
    pyautogui.click(x, y)
    time.sleep(1)

    # 复制好友的名字：文件传输助手
    pyperclip.copy(name)

    # 粘贴复制内容
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # 选中”文件传输助手“
    pyautogui.hotkey("enter")


# 向好友发送信息
def send_msg(msg):
    # 复制消息
    pyperclip.copy(msg)

    # 粘贴消息
    pyautogui.hotkey("ctrl", "v")

    # 发送消息
    pyautogui.hotkey("enter")


# 主要程序
time.sleep(2)
x, y = findImg()
send_name_to_search(x, y, "文件传输助手")
send_msg("hello python")
time.sleep(1)
send_msg("hello world")
time.sleep(1)
