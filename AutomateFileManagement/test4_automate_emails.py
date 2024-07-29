# @time     ：2024/7/25 14:58
# @author   : 莉光哈哈哈
# @file     : test4_automate_emails.py
# @software : PyCharm
'''
自动发送电子邮件
'''
'''
1.发送个性化电子邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_personalized_email(sender_email, sender_password, recipients, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    for recipient_email in recipients:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(sender_email, recipient_email, message.as_string())

    server.quit()


'''
2.发送带附件的电子邮件
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, file_path):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment;filename={file_path}")
        message.attach(part)

    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()


'''
3.自动电子邮件提醒
'''
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta


def send_reminder_email(sender_email, sender_password, recipient_email, subject, body, reminder_date):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    now = datetime.now()
    reminder_date = datetime.strptime(reminder_date, '%Y-%m-%d')

    if now.date() == reminder_date.date():
        message = MIMEText(body, 'plain')
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()
