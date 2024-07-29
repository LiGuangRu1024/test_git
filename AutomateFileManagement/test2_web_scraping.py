# @time     ：2024/7/25 14:25
# @author   : 莉光哈哈哈
# @file     : test2_web_scraping.py
# @software : PyCharm
'''
网页抓取
'''
'''
1.从网站中提取数据
'''
import requests
from bs4 import BeautifulSoup


def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # 此处编写代码，从网站中抓取相关数据


'''
2.批量下载图片
'''
import requests


def download_images(url, save_directory):
    response = requests.get(url)
    if response.status_code == 200:
        images = response.json()  # 假设API返回图片URL的JSON数组
        for index, image_url in enumerate(images):
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(f"{save_directory}/image_{index}.jpg", 'wb') as f:
                    f.write(image_response.content)


'''
3.自动提交表单
'''
import requests


def submit_form(url, form_data):
    response = requests.post(url, data=form_data)
    if response.status_code == 200:
        # 此处编写代码以处理表单提交后的响应
        pass


