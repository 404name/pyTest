# -*- coding = utf-8 -*-
# @Time : 2021/12/9 11:26
# @Author : Ram
# @File : Weather.py
# @Software : PyCharm
import requests



myproxies = {
    'http': 'http://180.97.34.35:80',
    'https': 'http://180.97.34.35:80'
}

def main():
    sentMsg("hello")

    
def sentMsg(msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # api_url = "https://qmsg.zendee.cn/group/49bdb9375842537a41ebc635a09229b2?msg= %s" % msg
    api_url = "https://qmsg.zendee.cn/send/49bdb9375842537a41ebc635a09229b2?msg= %s" % msg
    return requests.post(api_url, headers=headers, timeout=None).content



if __name__ == "__main__":
    main()
