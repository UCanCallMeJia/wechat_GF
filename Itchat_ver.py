import requests
import itchat
from random import choice
import time


def get_response(_info):
    print(_info)                                       # 从好友发过来的消息
    api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址
    data = {
        'key': '453b2da4ec4f4bec947fda36f6e1eedf',     # 如果这个 apiKey 如不能用，那就注册一次
        'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人
        'userid': 'wechat-robot',                      # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json()       # 把data数据发
    print(r.get('text'))                               # 机器人回复给好友的消息
    return r

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)




    # return "1" + get_response(msg["Text"])["text"]

if __name__ == '__main__':
    itchat.auto_login()                  # hotReload = True, 保持在线，下次运行代码可自动登录  hotReload=True
    itchat.set_chatroom_name()
    say_good_night = ''
    with open(r"D:\python_ws\GirlFriend\sentence_good_dream.txt", "r",encoding='UTF-8') as f:
        say_good_night = f.readlines()
    # print(say_good_night)

    mygirl = itchat.search_friends('温馨的冬夜')[0]['UserName']
    # print(mygirl)
    while True:
        print("守护中，时间:%s"% time.ctime())
        now_time = time.ctime()[-13:-8]
        print(now_time)

        # 每天晚23：10发晚安问候
        if now_time == '23:00':
            good_night = choice(say_good_night)
            print(good_night)
            itchat.send(good_night,toUserName=mygirl)

        

        time.sleep(60)
    
    
