# @time     ：2024/7/15 14:20
# @author   : 莉光哈哈哈
# @file     : test45_run_in_browsers.py
# @software : PyCharm
'''
多浏览器兼容性测试
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def run_test_in_browser(browser_name, url):
    if browser_name == 'chrome':
        service = Service('/path/to/chromedriver')
        driver = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        service = Service('/path/to/geckodriver')
        driver = webdriver.Firefox(service=service)
    elif browser_name == 'edge':
        service = Service('/path/to/msedgedriver')
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Unsupported browser")

    try:
        driver.get(url)
        title = driver.title
        assert "Python" in title, f"Expected 'Python' in page title,got '{title}'"
        print(f"Test passed in {browser_name}.")
    finally:
        driver.quit()


# 测试url
url = 'https://www.python.org'

# 测试不同的浏览器
run_test_in_browser("chrome", url)
run_test_in_browser("firefox", url)
run_test_in_browser("edge", url)
