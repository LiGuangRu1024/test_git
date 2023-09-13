# 时间：2023/8/28 10:20
# 人员: 莉光哈哈哈

import pytest
import requests


# def access_token():
#     URL = 'https://api.weixin.qq.con/cgi-bin/token?grant_type=client_credential&appid=wx7002cc0a80&secret' \
#           '=903b6b342003a5a9'
#     # 发送get请求
#     rep = requests.get(URL)
#     print(rep.text)
#     # 断言响应状态码为200，协议层断言
#     assert 200 == rep.status_code
#     rep_json = rep.json()
#     # 断言返回具体业务信息，数据业务层断言
#     assert 7200 == rep_json['expires_in']
#     # 断言请示响应总时间小于3s，性能断言
#     assert rep.elapsed.total_seconds() < 3
#
#     return rep_json['access_token']
#
#
# def test_createtag():
#     URL = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=' + access_token()
#     data = {"tag": {"name": "000"}}
#     rep = requests.post(url=URL, json=data)
#     assert 200 == rep.status_code
#     json_rep = rep.json()
#     assert '000' == json_rep['tag']['name']

# def test_createtag_F_errortoken():
#     URL = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=111'
#     rep = requests.get(URL)
#     assert 200 == rep.status_code
#     assert 40001 == rep.json()['errcode']
#
#
# if __name__ == '__main__':
#     pytest.main()
