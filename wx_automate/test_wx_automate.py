# @time     ：2024/8/9 14:47
# @author   : 莉光哈哈哈
# @file     : test_wx_automate.py
# @software : PyCharm
import time
import wxauto

wechat = wxauto.WeChat()

wechat.login()

friends = wechat.get_friends()


def send_message(friend_name, message):
    friend = friends[friend_name]
    friend.send_text(message)


def auto_reply(message):
    # 根据消息内容进行判断，返回相应的回复内容
    if "你好" in message:
        return "你好！请问有森马可以帮助你的吗?"
    elif "再见" in message:
        return "再见！祝你有美好的一天。"
    else:
        return "对不起，暂时不在线"


while True:
    new_messages = wechat.get_new_messages()
    for msg in new_messages:
        if msg.is_text():
            reply = auto_reply(msg.content)
            msg.reply(reply)
    time.sleep(5)  # 每五秒检查一次新消息
