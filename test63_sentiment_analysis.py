# @time     ：2024/8/19 14:08
# @author   : 莉光哈哈哈
# @file     : test63_sentiment_analysis.py
# @software : PyCharm
'''
自然语言处理---NLP
情感分析通常应用于社交媒体监控、产品评价分析、客户服务等
'''
import nltk
from textblob import TextBlob

# 下载必要的NLTK数据包
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"


# 示例评论数据
comments = [
    "this product is amazing",
    "I am really disappointed with the service",
    "the movie was quite entertaining",
    "i would not recommend this restaurant",
    "great job on the project",
    "terrible experience with the customer support"
]

# 对每条评论进行情感分析
for comment in comments:
    sentiment = analyze_sentiment(comment)
    print(f"Comment:'{comment}'-Sentiment:{sentiment}")
