# @time     ：2024/8/9 11:35
# @author   : 莉光哈哈哈
# @file     : test_gui.py
# @software : PyCharm
import time
import wxauto

from wx_automate.simple_gui import MyFrame

# 启动GUI应用程序
app = wx.App(False)
frame = MyFrame()
app.MainLoop()

# 准备测试脚本
auto = wxauto.Auto(block=True)  # block=True意味着自动化脚本会阻塞，等待操作完成

# 定位按钮控件
button = auto.window().find_by_name("button", recursive=True)

# 模拟点击按钮
button.click()

time.sleep(1)

# 验证标签的文本是否已更改
label = auto.window().find_by_name("label", recursive=True)
assert label.text() == "Hello,wxauto! you clicked the button"

# 关闭应用程序
auto.window().close()
