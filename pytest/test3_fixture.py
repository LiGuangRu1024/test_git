# 时间：2023/8/24 15:25
# 人员: 莉光哈哈哈
import pytest
import csv


@pytest.fixture()
def login():
    print("用户名linda密码登录")


def test_cart(login):
    print("用例1，登录后执行查看购物车其他功能")


def test_find_goods():
    print("用例2，不登录，执行浏览商品功能")


def test_pay(login):
    print("用例3：登录后执行支付功能")


# @pytest.fixture()
# def data():
#     test_data = {'name': 'linda', 'age': 18}
#     return test_data
#
#
# def test_login(data):
#     name = data['name']
#     age = data['age']
#     print("笔者的名字叫:{},今年{}。".format(name, age))

@pytest.fixture()
def read_data():
    with open("userinfo.csv") as f:
        row = csv.reader(f, delimiter=',')
        next(row)
        users = []
        for r in row:
            users.append(r)
    return users


# 只取文件中的第一组数据
def test_logins(read_data):
    name = read_data[0][0]
    age = read_data[0][1]
    print("笔者的名字叫:{},今年{}。".format(name, age))
