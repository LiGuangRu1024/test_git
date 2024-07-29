# @time     ：2024/7/26 17:33
# @author   : 莉光哈哈哈
# @file     : test13_QR_code.py
# @software : PyCharm
'''
1.基本二维码
'''
from MyQR import myqr

'''
words：内容
version：容错率
save_name：保存的名字
'''
myqr.run(words='https://www.baidu.com/',
         version=1,
         save_name='myqr.png')

'''
2.带图二维码
'''
from MyQR import myqr

'''
picture：生成二维码用到的图片
colorized：False 为黑白，True 为彩色
'''
myqr.run(words='https://www.baidu.com/',
         version=1,
         picture='640.jpg',
         colorized=True,
         save_name='pmyqr.png')

'''
3.动态二维码
'''
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    words="https://www.baidu.com",  # 可以是字符串，也可以是网址(前面要加http(s)://)
    version=1,  # 设置容错率为最高
    level='H',  # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    picture="640.gif",  # 将二维码和图片合成
    colorized=True,  # 彩色二维码
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    brightness=1.0,  # 用来调节图片的亮度，其余用法和取值同上
    save_name="640test.gif",  # 保存文件的名字，格式可以是jpg,png,bmp,gif
    save_dir=os.getcwd()  # 控制位置
)