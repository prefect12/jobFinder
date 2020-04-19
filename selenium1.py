# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:23:10 2020

@author: Administrator
"""
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import chardet
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome('I:\personal_project\Spider\chromedriver.exe')
browser.get ('https://www.shixiseng.com/intern/inn_zybhtcmv8dwu?pcm=pc_SearchList&mxa=asdd.0eqlx1._.$2')
title = browser.find_element_by_class_name('new_job_name').text
time = browser.find_element_by_class_name("job_date").find_element_by_tag_name('span')
salary = browser.find_element_by_class_name('job_msg').find_element_by_tag_name('span')
time.screenshot('./image/'+title +'_Time.png')
salary.screenshot('./image/'+title+'_Salary.png')


#def getSoup(baseUrl):
#    headers = {
#            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#            'accept-encoding': 'gzip, deflate, br',
#            'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
#            'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
#            }
#    
#    r = requests.get(baseUrl,headers=headers)
#    r.encoding = 'utf-8'
#    content = BeautifulSoup(r.text,"html.parser")
#    return r,content
#
#url = 'https://www.shixiseng.com/intern/inn_u4n8q0v6zsrf?pcm=pc_SearchList'
#
#r,soup = getSoup(url)