# @time     ：2023/12/25 11:06
# @author   : 莉光哈哈哈
# @file     : test43_re.py
# @software : PyCharm
import re

# re.match.group()  # 返回匹配对象
# re.match().span()  # 获取匹配范围
# re.match().start()  # 匹配开始位置
# re.match().end()  # 匹配结束位置

# 1、将正则表达式编译成一个pattern对象
pattern = re.compile('\d+')

# 2、匹配字符串
str1 = '12hello 456,a;b'
m1 = pattern.match(str1)

# 3、获取
print(m1)  # <re.Match object; span=(0, 2), match='12'>
print(m1.group())  # 12
print(m1.span())  # (0,2)
print(m1.start())  # 0
print(m1.end())  # 2

# 一、re模块常用方法
'''
1、该方法用来生成正则表达式对象，其语法格式如下:
'''
'''
参数说明：
pattern：正则表达式对象
flags：代表功能标志位，扩展正则表达式的匹配
'''
regex = re.compile(pattern, flags=0)

'''
2、根据正则表达式匹配目标字符串内容
该函数的返回值是匹配到的内容列表，如果正则表达式有子组，则只能获取到子组对应的内容
参数说明如下：
pattern：正则表达式对象
string：目标字符串
flags：代表功能标志位，扩展正则表达式的匹配
'''
re.findall(pattern, string='', flags=0)

'''
3、该函数根据正则表达式对象匹配目标字符串内容。
参数说明：
string：目标字符串
pos：获取目标字符串的开始匹配位置
endpos：截取目标字符串的结束匹配位置
'''
regex.findall(string='', pos=0, endpos=2)

'''
4、该函数使用正则表达式匹配内容，切割目标字符串。返回值是切割后的内容列表。
参数说明：
pattern：正则表达式
string：目标字符串
flags：功能标志位，扩展正则表达式的匹配
'''
re.split(pattern, string='', flags=0)

'''
5、该函数使用一个字符串替换正则表达式匹配到的内容，返回值是替换后的字符串。
其参数说明：
pattern：正则表达式
replace：替换的字符串
string：目标字符串
max：最多替换几处，默认替换全部
flags：功能标志位，扩展正则表达式的匹配
'''
# re.sub(pattern,replace,string,max,flags=0)

'''
6、匹配目标字符串第一个符合的内容，返回值为匹配的对象。
参数说明：
pattern：正则表达式
string：目标字符串
'''
re.search(pattern, string='', flags=0)

# 二、正则表达式中的分组
'''
分组时通过（）来表示的，一个括号就表示一个分组
'''
"""
(1)筛选特定内容
取分组内容可以通过match对象的group方法来取
group(1)表示取正则表达式中第一个括号的内容，依次类推
"""
import re

content = '{name:"zhangsan",age:"10",hobby["basktball","football","read"]}'
pattern = re.compile(r'{name:"(\w+)",age:"(\d+)".+}')
match = pattern.search(content)
print(match.group(1))  # zhangsan
print(match.group(2))  # 10
print("---------------------------------------------------------------------------------")

"""
(2)可以在同一个表达式的后面引用前面的分组表达式
"""
import re

s = "<html><h1>正则表达式</h1></html>"
pattern = re.compile(r'<(html)><(h1)>(.*)</\2></\1>')
match = pattern.search(s)
print(match.group(3))  # 正则表达式
