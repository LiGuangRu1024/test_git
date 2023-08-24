# 时间：2023/8/24 16:19
# 人员: 莉光哈哈哈
import pytest
import smtplib


# 做清理操作
@pytest.fixture()
def smtp_connection_yield():
    with smtplib.SMTP("smtp.163.com", 25, timeout=5) as smtp_connection:
        print("------------------start connection")
        yield smtp_connection
        print("------------------end connection")


def test_send_email(smtp_connection_yield):
    print("发邮件")
