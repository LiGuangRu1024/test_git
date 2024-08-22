# @time     ：2024/8/19 14:25
# @author   : 莉光哈哈哈
# @file     : test64_detect_sql_inject.py
# @software : PyCharm
'''
SQLmap检测和利用SQL注入漏洞
'''

'''
关键组件
1. 解析命令行参数
sqlmap.py: 这个文件负责解析命令行参数，并根据这些参数初始化 SQLmap 的运行环境。

lib/core/settings.py: 包含了全局设置和默认配置。

2. 发送 HTTP 请求
lib/core/settings.py: 包含了默认的 HTTP 头信息和其他请求配置。

lib/core/requesthandler.py: 负责发送 HTTP 请求和处理响应。

3. 检测 SQL 注入
lib/core/inject.py: 负责检测 SQL 注入漏洞。

lib/core/data.py: 存储全局变量和数据结构，如当前使用的 DBMS 类型、注入类型等。

lib/core/settings.py: 包含了各种默认设置，如默认的注入技术、数据库类型等。

4. 利用 SQL 注入
lib/core/inject.py: 根据检测到的 SQL 注入漏洞，尝试利用这些漏洞来获取数据库信息。

lib/core/settings.py: 包含了利用 SQL 注入所需的默认设置。

5. 枚举数据
lib/core/inject.py: 包含了枚举数据库、表、字段和数据的方法。

lib/core/data.py: 存储了枚举过程中获取的信息。

6. 处理响应
lib/core/responseparser.py: 负责解析 HTTP 响应，判断是否存在 SQL 注入漏洞。

lib/core/settings.py: 包含了默认的响应处理逻辑。
'''

# 假设这是简化版的inject.py中的一部分
def detect_injection(url):
    # 初始化HTTP请求
    headers, proxies, timeout = get_settings().get_http_options()

    # 发送原始请求
    response = send_request(url, headers=headers, proxies=proxies, timeout=timeout)

    # 构建注入测试字符串
    injection_string = build_injection_string()

    # 发送带有注入字符串的请求
    injected_response = send_request(url + injection_string, headers=headers, proxies=proxies, timeout=timeout)

    # 分析响应差异
    if is_injection_detected(response, injected_response):
        return True

    return False


def build_injection_string():
    # 构建注入字符串
    # 这里可以根据不同的DBMS和注入类型构建不同的注入字符串
    return "'OR 1=1 --'"


def is_injection_detected(original_response, injected_response):
    # 分析两个响应之间的差异
    # 例如，检查响应长度、状态码等
    if len(original_response) != len(injected_response):
        return True

    return False
