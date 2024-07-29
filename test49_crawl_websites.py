# @time     ：2024/7/17 10:14
# @author   : 莉光哈哈哈
# @file     : test49_crawl_websites.py
# @software : PyCharm
'''
pip install requests beautifulsoup4
'''

import requests
from bs4 import BeautifulSoup
import os


def fetch_video_url(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 解析HTML文档
    soup = BeautifulSoup(response.text, 'html.parser')
    # 查找视频标签
    video_tag = soup.find('video')
    # 获取视频源链接
    video_url = video_tag['src'] if video_tag else None
    return video_url


def download_video(video_url, save_path):
    # 检查目录是否存在，不存在则创建
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))

    # 发送请求并下载视频
    with open(save_path, 'wb') as f:
        response = requests.get(video_url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                print('\r[%s%s]' % ('=' * done, ' ' * (50 - done)), end='')


if __name__ == '__main__':
    url = "http://example.com/video-page"
    video_url = fetch_video_url(url)

    if video_url:
        save_path = "./videos/video.mp4"
        download_video(video_url, save_path)
        print("Video downloaded successfully.")
    else:
        print("No video found on the page.")
