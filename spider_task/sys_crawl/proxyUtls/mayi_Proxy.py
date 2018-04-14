# coding:utf8
import sys

import time
import hashlib

from pip._vendor import requests


def generate_sign():
    appkey = "xxxx"
    secret = "xxxxxx"
    mayi_url = "xxxxxx"
    mayi_port = "xxxxxxx"
    mayi_proxy = 'http://{}:{}'.format(mayi_url, mayi_port)

    paramMap = {
        "app_key": appkey,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    keys = sorted(paramMap)
    codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)

    sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

    paramMap["sign"] = sign

    keys = paramMap.keys()
    authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)
    return authHeader, mayi_proxy


def proxy_test():
    authHeader, mayi_proxy = generate_sign()
    headers = {
        "Proxy-Authorization": authHeader,
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"
    }

    proxies = {
        "http": mayi_proxy,
        "https": mayi_proxy,
    }
    chushou_url = "http://s.m.taobao.com/search?m=api4h5&nick=%E7%92%90%E7%92%90%E5%98%89%E5%98%89&n=40&page=1"
    response = requests.get(chushou_url, proxies=proxies, headers=headers, allow_redirects=False, verify=False)

    print (response.status_code)
    print (response.headers)
    print (response.text)


if __name__ == "__main__":
    proxy_test()
