# @time     ：2024/7/26 10:39
# @author   : 莉光哈哈哈
# @file     : test7_automate_system_tasks.py
# @software : PyCharm
'''
1.管理系统进程
'''
import psutil


def get_running_processes():
    return [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]


def kill_process_by_name(process_name):
    for p in psutil.process_iter(['pid', 'name', 'username']):
        if p.info['name'] == process_name:
            p.kill()


'''
2.使用Cron安排任务
'''
from crontab import CronTab


def schedule_task(command, schedule):
    cron = CronTab(user=True)
    job = cron.new(command=command)
    job.setall(schedule)
    cron.write()


'''
3.监控磁盘空间
'''
import psutil


def check_disk_space(minium_threshold_gb):
    disk = psutil.disk_usage('/')
    free_space_gb = disk.free / (2 ** 30)  # 将字节转换成GB

    if free_space_gb < minium_threshold_gb:
        # 此处编写代码以发送警告（电子邮件、通知等）
        pass
