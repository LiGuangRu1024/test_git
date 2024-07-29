# @time     ：2024/7/29 10:14
# @author   : 莉光哈哈哈
# @file     : test14_automate_read_WebNews.py
# @software : PyCharm
'''
自动化读取网页新闻-----一个是用于网络抓取的库（如BeautifulSoup和requests），另一个是用于文本转语音的库（如gTTS）。
'''
import pylab as p
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os


# 爬取网页文本内容
def fetch_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # 从网页中提取文本内容
    paragraphs = soup.find_all("p")
    text = "\n".join([p.text for p in paragraphs])

    return text


# 将文本转换为语音并播放
def text_to_speech(text, language="en"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("temp_audio.mp3")

    # 播放生成的音频文件
    os.system("mpg123 temp_audio.mp3")


if __name__ == "__main__":
    url = "https://example.com/article"  # 将此转换为你想要抓取的网页url

    # 抓取网页文本
    text = fetch_text_from_url(url)

    # 将抓取到的文本转换为语音并播放
    text_to_speech(text)
