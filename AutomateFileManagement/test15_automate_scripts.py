# @time     ：2024/7/29 10:35
# @author   : 莉光哈哈哈
# @file     : test15_automate_scripts.py
# @software : PyCharm
'''
1.批量文件重命名
'''
import os


def batch_rename(path, prefix='', suffix=''):
    for i, filename, in enumerate(os.listdir(path)):
        new_name = f"{prefix}{i:03d}{suffix}{os.path.splitext(filename)[1]}"
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_name)
        os.rename(old_file, new_file)


# 使用示例
batch_rename('/path/to/your/directory', 'file_', '.txt')

'''
2.定时任务自动化执行
'''
import schedule
import time


def job_to_schedule():
    print("当前时间：", time.ctime(), "任务正在执行。。。。")


# 定义每天9点执行任务
schedule.every().day.at("09:00").do(job_to_schedule)

while True:
    schedule.run_pending()
    time.sleep(1)

# 使用示例：运行此脚本后，每天上午九点会自动打印当前时间及提示信息

'''
3.数据库操作自动化
'''
import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"成功连接到SQLite数据库：{db_file}")
    except Error as e:
        print(e)

    return conn


def insert_data(conn, table_name, data_dict):
    keys = ','.join(data_dict.keys())
    values = ','.join(f"'{v}'" for v in data_dict.values())

    sql = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("数据插入成功")
    except sqlite3.Error as e:
        print(e)


# 使用示例
conn = create_connection("my_database.db")
data = {'name': 'ANNA', 'age': 39}
insert_data(conn, 'users', data)

# 在适当时候关闭数据库连接
conn.close()

'''
4.网页内容自动化抓取
'''
import requests
from bs4 import BeautifulSoup


def fetch_web_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 示例提取页面标题
        title = soup.find('title').text
        return title
    else:
        return "无法获取网页内容"


# 使用示例：
url = 'https://example.com'
web_title = fetch_web_content(url)
print("网页标题：", web_title)

'''
5.图片批量压缩
'''
from PIL import Image
import os


def compress_images(dir_path, quality=90):
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(dir_path, filename))
            img.save(os.path.join(dir_path, f'compressed_{filename}'), optimize=True, quality=quality)


# 使用示例
compress_images('/path/to/your/images', quality=50)

'''
6.日志文件分析自动化
'''


def analyze_log(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    error_count = 0
    for line in lines:
        if 'ERROR' in line:
            error_count += 1

    print(f"日志文件中包含{error_count}条错误记录")


# 使用示例
analyze_log('application.log')

'''
7.数据可视化自动化
'''
import matplotlib.pyplot as plt
import pandas as pd


def visualize_data(data_file):
    df = pd.read_csv(data_file)

    # 示例：绘制柱状图
    df.plot(kind='bar', x='category', y='value')
    plt.title("数据分布")
    plt.xlabel("类别")
    plt.ylabel("值")
    plt.show()


# 使用示例
visualize_data('data.csv')

'''
8.邮件附件批量下载
'''
import imaplib
import email
from email.header import decode_header
import os


def download_attachments(email_addr, password, imap_server, folder="INBOX"):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_addr, password)

    mail.select(folder)
    result, data = mail.uid('search', None, 'ALL')
    uids = data[0].split()

    for uid in uids:
        _, msg_data = mail.uid('fetch', uid, '(RFC822)')
        raw_email = msg_data[0][1].decode('utf-8')
        email_message = email.message_from_string(raw_email)

        for part in email_message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            if bool(filename):
                file_data = part.get_payload(decode=True)
                with open(os.path.join('/path/to/download', filename), 'wb') as f:
                    f.write(file_data)

        mail.close()
        mail.logout()


# 使用示例
download_attachments('your-email@example.com', 'your-password', 'imap.example.com')

'''
9.定时发送报告自动化
'''
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def generate_report(source, to_addr, subject):
    # 假设这里是从数据库或文件中获取数据并生成报告内容
    report_content = pd.DataFrame({"Data": [1, 2, 3], "Info": ["A", "B", "C"]}).to_html()

    msg = MIMEMultipart()
    msg['From'] = 'your-email@example.com'
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(report_content, 'html'))

    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login('your-email@example.com', 'your-password')
    text = msg.as_string()
    server.sendmail('your-email@example.com', to_addr, text)
    server.quit()


# 使用示例----结合前面的定时任务脚本，可实现定时发送功能
generate_report('data.csv', 'receiver@example.com', "每日数据报告")

'''
10.自动化性能测试
'''
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)  # 定义用户操作之间的等待时间

    @task
    def load_test_api(self):
        response = self.client.get('/api/data')
        assert response.status_code == 200

    @task(3)  # 指定该任务在总任务中的执行频率是其他任务的3倍
    def post_data(self):
        data = {"key": "value"}
        response = self.client.post("/api/submit", json=data)
        assert response.status_code == 201

# 运行Locust命令启动性能测试
# locust -f your_test_script.py --host=http://your-api-url.com


'''
11.自动化部署与回滚脚本-----# 对于回滚操作，可以基于版本控制系统实现或创建备份，在出现问题时恢复上一版本的部署。
'''
from fabric import Connection

def deploy(host_string,user,password,project_path,remote_dir):
    c=Connection(host=host_string,user=user,connect_kwargs={"password":password})

    with c.cd(remote_dir):
        c.run('git pull origin master')  # 更新代码
        c.run('pip install -r requirements.txt')  # 安装依赖
        c.run('python manage.py migrate')  # 执行数据库迁移
        c.run('python manage.py collectstatic --noinput')  # 静态文件收集
        c.run('supervisorctl restart your_project_name')  # 重启服务

# 使用示例：
deploy(
    host_string='your-server-ip',
    user='deploy_user',
    password='deploy_password',
    project_path='/path/to/local/project',
    remote_dir='/path/to/remote/project'
)
