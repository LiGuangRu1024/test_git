# 时间：2023/6/6 14:55
# 人员: 莉光哈哈哈


import schedule
import time

def job():
    print("哈哈哈哈哈--------------------------")

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)