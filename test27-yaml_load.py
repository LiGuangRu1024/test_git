# 时间：2023/6/10 17:30
# 人员: 莉光哈哈哈

# import yaml
# print(yaml.safe_load("""
#  - Hesperiidae
#  - Papilionidae
#  - Apatelodidae
#  - Epiplemidae
#  """,Loader=yaml.FullLoader))

# import yaml
# print(yaml.safe_load("""
#  - Hesperiidae
#  - Papilionidae
#  - Apatelodidae
#  - Epiplemidae
#  """))

# import yaml
# print(yaml.safe_load(open("test27.yml")))

# import yaml
# print(yaml.dump([['Hesperiidae', 'Papilionidae'], 'Apatelodidae', 'Epiplemidae', {'a': 1}]))


import yaml
with open("test27.yml", "w") as f:
    yaml.dump(data={'a': [1, 2]}, stream=f)