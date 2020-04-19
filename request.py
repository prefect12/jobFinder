# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:48:40 2020

@author: Administrator
"""

#普通
import requests
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(r.text)
print(r.cookies)



#添加参数
import requests

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
        'city':'全国',
        'internExtend':''
        }

headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

baseUrl = 'https://www.shixiseng.com/interns?'

r = requests.get(baseUrl,params=params,headers = headers)
print(r.text)


#request 对象
from requests import Request,Session
url = 'https://www.shixiseng.com/interns?'
s = Session()
req = Request('GET',url,headers = headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)