# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:48:40 2020

@author: Administrator
"""
import re,requests



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
r.encoding = 'utf-8'
content = r.text

#漂亮汤
#url = 'https://www.google.com/search?q=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B5%8B%E8%AF%95&rlz=1C1CHBD_zh-CNAU838AU838&oq=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B5%8B%E8%AF%95&aqs=chrome..69i57j0l7.9159j0j8&sourceid=chrome&ie=UTF-8'

#content = requests.get().text
from bs4 import BeautifulSoup
soup = BeautifulSoup(content,"html.parser")



#for i in soup.find_all(class_=['intern-wrap intern-item','intern-wrap intern-item is-view']):
#    for j in i:
#        print(j)

i = soup.find_all(class_=['intern-wrap intern-item','intern-wrap intern-item is-view'])[0]
page = soup.find_all(class_='number')
list(range(page[-1].text)))


