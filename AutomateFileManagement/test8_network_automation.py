# @time     ：2024/7/26 14:17
# @author   : 莉光哈哈哈
# @file     : test8_network_automation.py
# @software : PyCharm
'''
1.检查网络状态
'''
import requests


def check_website_status(url):
    response = requests.get(url)
    if response.status_code == 200:
        # 在此处编写代码已处理成功的响应
        pass
    else:
        # 在此处编写以处理不成功的响应
        pass


'''
2.自动化FTP传输
'''
from ftplib import FTP


def ftp_file_transfer(host, username, password, local_file_path, remote_file_path):
    with FTP(host) as ftp:
        ftp.login(user=username, passwd=password)
        with open(local_file_path, 'rb') as f:
            ftp.storbinary(f'STOR{remote_file_path}', f)


'''
3.网络设备配置-----脚本使用netmiko库自动配置网络设备，脚本将在目标设备上执行它们
'''
from netmiko import ConnectHandler


def configure_network_device(host, username, password, configuration_commands):
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }

    with ConnectHandler(device) as net_connect:
        net_connect.send_config_set(configuration_commands)
