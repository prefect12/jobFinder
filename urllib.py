# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 18:59:44 2020

@author: Administrator
"""
#openner = urllib.request.build_opener()
#openner.add_handler()
import requests
import urllib.request
import urllib.parse
import socket
import urllib.error

url = 'https://www.shixiseng.com/interns?page=1&keyword=Python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E6%AD%A6%E6%B1%89&internExtend='
testUrl = 'https://www.seek.com.au/Python-jobs/in-All-Melbourne-VIC'

headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

request = urllib.request.Request(url=testUrl,headers= header)

try:
    response = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    print(e)

web = response.read().decode('utf-8')
print(web)


# 代理 Proxy

from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

#本机代理
proxyHandler = ProxyHandler({
        'http':'http://123.55.4.179:9999',
        'https':'https://123.55.4.179:9999'
        })

url = 'https://www.shixiseng.com/interns?page=1&keyword=Python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E6%AD%A6%E6%B1%89&internExtend='
opener = build_opener(proxyHandler)

try :
    response = opener.open(url)
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e)


#URL 分析
from urllib.parse import urlparse,urlunparse,urlsplit,urlunsplit

url = 'http://www.baidu.com/index.html;user?a=6#comment'

result = urlparse(url)
print(result)

result = urlsplit(url)
print(result)

data =['http','www.baidu.com ','index.html','user','a=6', 'comment']
print(urlunparse(data))



#禁忌炼金术
from urllib.parse import urlencode

params = {
        'page':'1',
        'keyword':'Python',
        'type':'intern',
        'area':'',
        'months':'',
        'days':'',
        'degree':'',
        'official':'',
        'enterprise':'',
        'salary':'',
        'publishTime':'',
        'sortType':'',
        'city':'武汉',
        'internExtend':''
        }

baseUrl = 'https://www.shixiseng.com/interns?'
url = baseUrl + urlencode(params)
print(url)

#quote
from urllib.parse import quote
keyword = '武汉'
print(quote(keyword))
