# @time     ：2023/12/15 14:19
# @author   : 莉光哈哈哈
# @file     : test10_json.py
# @software : PyCharm
# # 从python到json
# import json
#
# person = {
#     'name': 'Jack',
#     'age': 30,
#     'city': 'New York',
#     'hasChildren': False,
#     'titles': ['engineer', 'programmer'],
# }
#
# # 转换为json字符串
# person_json = json.dumps(person)
#
# # 指定其他参数
# person_json2 = json.dumps(
#     person,
#     indent=4,
#     separators=(':', '='),
#     sort_keys=True,
# )
#
# # 打印
# print(person_json)
# print(person_json2)
#
# with open('./data/person.json', 'w') as f:
#     json.dump(person, f)
# print("---------------------------------------------------------------")

# 从json到python
# import json
#
# # json字符串
# # person_json = """
# # {
# #     'name': 'Jack',
# #     'age': 30,
# #     'city': 'New York',
# #     'hasChildren': False,
# #     'titles': [
# #         'engineer',
# #         'programmer'
# #     ]
# # }
# # """
# # # 转为python对象
# # person = json.loads(person_json)
# # print(person)
#
# with open('./data/person.json', 'r') as f:
#     person = json.load(f)
#     print(person)
# print("----------------------------------------------------------------")

# 自定义编码
# import json
#
#
# def encode_complex(z):
#     if isinstance(z, complex):
#         # 仅仅是类名的键是重要的，值可以是任意的
#         return {z.__class__.__name__: True, 'real': z.real, 'imag': z.imag}
#     else:
#         raise TypeError(f"'{z.__class__.__name__}'不是指定的格式")
#
#
# z = 6 + 9j
# zJSON = json.dumps(z, default=encode_complex)
# print(zJSON)
# print("----------------------------------------------------------------")

# import json
# from json import JSONEncoder
#
#
# class ComplexEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(z, complex):
#             return {z.__class__.__name__: True, 'real': z.real, 'imag': z.imag}
#         # 让父类的默认方法处理其他对象，或者抛出一个 TypeError
#         return JSONEncoder.default(self, o)
#
#
# z = 8 + 9j
# zJSON = json.dumps(z, cls=ComplexEncoder)
# print(zJSON)
# # 或者直接使用编码器
# zJson = ComplexEncoder().encode(z)
# print(zJson)
# print("------------------------------------------------------------------")
# 解码
# import json
#
# zJSON = '{"complex":true,"real":9.0,"imag":8.0}'
#
# z = json.loads(zJSON)
# # 默认为字典类型
# print(type(z))
# print(z)
#
#
# def decode_complex(dct):
#     if complex.__name__ in dct:
#         return complex(dct['real'], dct['imag'])
#     return dct
#
#
# # 现在，解码后的对象是复合类型的
# z = json.loads(zJSON, object_hook=decode_complex)
# print(type(z))
# print(z)
print("--------------------------------------------------------------------")
# 通过对象解码、编码函数
import json


class User:
    # 自定义类，并且在__init__()中指定所有变量
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends


class Player:
    # 另外一个自定义类
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level


def encode_obj(obj):
    '''
    接受一个自定义对象并返回该对象的字典表示。
    此dict表示还包括对象的模块和类名
    :param obj:
    :return:
    '''
    # 将对象的模块和类名添加到字典中
    obj_dict = {
        "__class__": obj.__class__.__name__,
        "__module__": obj.__module__,
    }
    # 用对象属性更新字典
    obj_dict.update(obj.__dict__)
    return obj_dict


def decode_dct(dct):
    '''
    接受一个字典并返回一个与该字典关联的自定义对象。
    它利用字典中的“__module__”与“__class__”元数据
    知道要创建哪种对象类型
    :param dct:
    :return:
    '''
    if "__class__" in dct:
        # 将字典中的"__module__"和“__class__”元数据删除，以便只保留实例参数
        class_name = dct.pop("__class__")
        module_name = dct.pop("__module__")
        # 我们使用内建的__import__函数，因为模块名称在运行时还不知道
        module = __import__(module_name)
        # 在模块总查找类名
        class_ = getattr(module, class_name)
        # 用字典解包的方式初始化对象
        # 注意，这只是在类的所有__init__()参数都是字典键时才能工作
        obj = class_(**dct)
    else:
        obj = dct
    return obj


# User类使用我们的编码和解码方法
user = User(
    name='John',
    age=28,
    friends=['Jane', 'Tom'],
    balance=20.90,
    active=True,
)
userJSON = json.dumps(
    user,
    default=encode_obj,
    indent=4,
    sort_keys=True,
)
print(userJSON)
user_decoded = json.loads(
    userJSON,
    object_hook=decode_dct,
)
print(type(user_decoded))
# Player类使用我们的编码和解码方法
player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(
    player,
    default=encode_obj,
    indent=4,
    sort_keys=True,
)
print(playerJSON)
player_decoded = json.loads(
    playerJSON,
    object_hook=decode_dct,
)
print(type(player_decoded))
