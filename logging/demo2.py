# @time     ：2023/10/20 14:08
# @author   : 莉光哈哈哈
# @file     : demo2.py
# @software : PyCharm
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# # test1-------第三方SMTP服务
# mail_host = 'smtp.xxx.com'  # 设置服务器
# mail_user = 'xxx'  # 用户名
# mail_pass = 'xxx'  # 口令
#
# sender = 'from@runoob.com'
# receivers = ['1498695215@qq.com']
#
# message = MIMEText('python邮件发送测试', 'plain', 'utf-8')
# message['From'] = Header('菜鸟教程', 'utf-8')
# message['To'] = Header('测试', 'utf-8')
#
# subject = 'python smtp 测试'
# message['subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("error：无法发送邮件")

# test2---------QQ邮件测试发送
# uqbtswloufkzjech

# my_sender = '1498695215@qq.com'  # 发件人邮箱账号
# my_pass = 'uqbtswloufkzjech'  # 发件人邮箱密码
# my_user = '766178770@qq.com'  # 收件人邮箱账号


# def mail():
#     ret = True
#     try:
#         msg = MIMEText('python邮件发送测试', 'plain', 'utf-8')
#         msg['From'] = formataddr(["Lhia", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题
#
#         server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()  # 关闭连接
#     except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret = False
#     return ret
#
#
# ret = mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")


# # test3----------发送带附件的邮件
# sender = '1498695215@qq.com'
# sender_pass = 'uqbtswloufkzjech'
# receivers = ['1498695215@qq.com']


# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header('Lhia <1498695215@qq.com>')
# message['To'] = Header('Lhia <1498695215@qq.com>')
# subject = 'python smtp邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# message.attach(MIMEText('这是python邮件发送测试。。。。', 'plain', 'utf-8'))
#
# # 构造附件1，传送当前目录下的test.txt文件
# att1 = MIMEText(open('demo2.txt', 'rb').read().decode('utf-8'), 'base64', 'utf-8')
# att1['Content-Type'] = 'application/octet-stream'
# # 这里的filename随便写，写什么名字，邮件中显示什么名字
# att1['Content-Disposition'] = 'attachment;filename="demo2.txt"'
# message.attach(att1)
#
# try:
#     server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
#     server.login(sender, sender_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#     server.sendmail(sender, receivers, message.as_string())
#     server.quit()
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("error：无法发送邮件")


# test4----------发送带图片的邮件
sender = '1498695215@qq.com'
sender_pass = 'uqbtswloufkzjech'
receivers = ['1498695215@qq.com']

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header('Lhia <1498695215@qq.com>')
msgRoot['To'] = Header('Lhia <1498695215@qq.com>')
subject = 'python smtp邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img decoding="async" src="cid:image1"></p>

"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

try:
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(sender, sender_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sender, receivers, msgRoot.as_string())
    server.quit()
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")