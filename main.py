# CSDN自动签到
import requests, json, os

if __name__ == '__main__':
    url = 'https://me.csdn.net/api/LuckyDraw_v2/signIn'
    COOKIE = os.environ['COOKIE']
    headers = {
        "cookie": COOKIE,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
    }
    data = {
        "ip": "",
        "platform": "pc-my",
        "product": "pc",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "username": "weixin_42009804",
        "uuid": "10_36630242670-1594965914785-561624",
    }
    # 执行签到
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(response.text)
