# @time     ：2024/7/26 16:34
# @author   : 莉光哈哈哈
# @file     : test12_make_calculator.py
# @software : PyCharm
'''
实现基本的加、减、乘、除运算的计算器
'''
import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("简易计算器")
        self.geometry("400×400")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # 结果显示框
        result_entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=20, justify="right")
        result_entry.grid(row=0, column=0, columnspan=4)

        # 数字按钮
        button_font = ('Arial', 14)
        button_bg = "#ccc"
        button_active_bg = "#aaa"
        for i in range(9):
            button = tk.Button(self, text=str(i + 1), font=button_font, bg=button_bg, activebackground=button_active_bg,
                               command=lambda i=i: self.on_number_button_click(i + 1))
            button.grid(row=3 - i // 3, column=i % 3)

        zero_button = tk.Button(self, text="0", font=button_font, bg=button_bg, activebackground=button_active_bg,
                                command=lambda: self.on_number_button_click(0))
        zero_button.grid(row=4, column=1)

        # 运算符按钮
        operators = [
            ("+", 0, 3),
            ("-", 1, 3),
            ("*", 2, 3),
            ("/", 3, 3),
            ("=", 4, 3)
        ]
        for operator, row, col in operators:
            button = tk.Button(self, text=operator, font=button_font, bg=button_bg, activebackground=button_active_bg,
                               command=lambda operator=operator: self.on_operator_button_click(operator))
            button.grid(row=row, column=col)

        # 清除按钮
        clear_button = tk.Button(self, text="清除", font=button_font, bg=button_bg, activebackground=button_active_bg,
                                 command=self.on_clear_button_click)
        clear_button.grid(row=4, column=0)

        # 删除按钮
        delete_button = tk.Button(self, text="删除", font=button_font, bg=button_bg, activebackground=button_active_bg,
                                  command=self.on_delete_button_click)
        delete_button.grid(row=4, column=2)

    def on_number_button_click(self, number):
        current_result = self.result_var.get()
        if current_result == "0" or current_result[-1] in "+-*/":
            self.result_var.set(str(number))
        else:
            self.result_var.set(current_result + str(number))

    def on_operator_button_click(self, operator):
        current_result = self.result_var.get()
        if current_result[-1] in "+-*/":
            self.result_var.set(current_result[:-1] + operator)
        else:
            self.result_var.set(current_result + operator)

    def on_clear_button_click(self):
        self.result_var.set("0")

    def on_delete_button_click(self):
        current_result = self.result_var.get()
        if len(current_result) > 1:
            self.result_var.set(current_result[:-1])
        else:
            self.result_var.set("0")

    def on_equal_button_click(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(str(result))
        except ZeroDivisionError:
            self.result_var.set

