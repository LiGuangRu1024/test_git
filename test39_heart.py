# 时间：2023/8/21 14:52
# 人员: 莉光哈哈哈
import turtle as tu
import random as ra

tu.setup(1.0, 1.0)  # 设置画板大小（小数表示比例，整数表示大小）
tu.screensize(1, 1)  # 设置屏幕大小
tu.bgcolor('black')  # 设置画布背景颜色
t = tu.Pen()  # 设置画笔
t.ht()  # 隐藏画笔
colors = ['pink', 'hotpink', 'deeppink', 'lightpink']  # 爱心的颜色列表,可以设置自己喜欢的颜色噢


# colors = ['skyblue', 'lightblue', 'blue', 'royalblue'] # 蓝色系


class Love():  # 爱心类
    def __init__(self, r):  # 初始化
        self.r = r  # 爱心的半径
        self.x = 0  # 爱心的横坐标
        self.y = 120  # 爱心的纵坐标
        self.color = ra.choice(colors)  # 爱心的颜色
        self.outline = 2  # 爱心的外框大小（可不要）

    def draw(self):  # 画爱心函数，就是用turtle画爱心
        t.pensize(self.outline)
        t.penup()
        t.color(self.color)
        t.goto(self.x, self.y)
        t.pendown()
        # t.begin_fill()
        # t.fillcolor('pink')
        t.setheading(120)
        t.circle(self.r, 195)
        t.fd(self.r * 2.4)
        t.lt(90)
        t.fd(self.r * 2.4)
        t.circle(self.r, 195)
        # t.end_fill()

    def change(self):  # 改变爱心的大小（爱心不断增大）
        if self.r <= 100:
            self.r += 1
        else:
            self.r = 1
            self.x = 0
            self.y = 120
            self.c = ra.choice(colors)


Loves = []  # 爱心列表
for i in range(200):  # 循环增加爱心
    Loves.append(Love(i + 1))
while True:  # 开始画爱心
    tu.tracer(0)
    t.clear()
    for i in range(99):
        Loves[i].draw()
        Loves[i].change()
    tu.update()
tu.mainloop()
