# @time     ：2024/8/9 10:54
# @author   : 莉光哈哈哈
# @file     : simple_gui.py
# @software : PyCharm
'''
pip install wxPython
'''
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Simple GUI")
        panel = wx.Panel(self)
        self.label = wx.StaticText(panel, label="Hello,wxauto!", pos=(10, 10))
        self.button = wx.Button(panel, label="Click me", pos=(10, 50))
        self.button.Bind(wx.EVT_BUTTON, self.on_button_click)
        self.Show()

    def on_button_click(self, event):
        self.label.SetLabel("Hello,wxauto! You clicked the button")


app = wx.APP(False)
frame = MyFrame()
app.MainLoop()
