# @time     ：2023/11/22 16:38
# @author   : 莉光哈哈哈
# @file     : test4_test_login.py
# @software : PyCharm
import requests
import unittest
from ddt import ddt, file_data


@ddt
class CrmLogin(unittest.TestCase):
    @file_data("data/test_login.yaml")
    def test_login(self, method, url, header):
        # data = {
        #         "accountCode": "100021",
        #         "mobilePhone": "16688889999",
        #         "password": "123456",
        #         "originSystem": 1
        # },
        # res = requests.request(
        #     method=method,
        #     url=url,
        #     headers=header,
        #     json=data[0],
        #     verify=False
        # )
        # print(res.text)
        res = requests.request(
            method=method,
            url=url,
            headers=header,
            json={
                "accountCode": "100021",
                "mobilePhone": "16688889999",
                "password": "123456",
                "originSystem": 1
            },
            verify=False)
        print(res.text)


if __name__ == '__main__':
    unittest.main()
