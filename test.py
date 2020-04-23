# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:25:49 2020

@author: Administrator
"""
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
#import chardet
#import pymysql
#import pandas as pd

def getUrl(page=1,keyword='',area='',degree='',salary='',city='全国'):
        baseUrl = 'https://www.shixiseng.com/interns?'
        
        params = {
        'page':'',
        'keyword':'',
        'type':'intern',
        'area':'',
        'months':'',
        'days':'',
        'degree':'',
        'official':'',
        'enterprise':'',
        'salary':'-0',
        'publishTime':'',
        'sortType':'',
        'city':'',
        'internExtend':''
        }
        
        params['page'] = page
        params['keyword'] = keyword
        params['area'] = area 
        params['degree'] = degree
        params['city'] = city
        
        url = baseUrl + urlencode(params)
        
        return url

def getSoup(baseUrl):
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
                }
        
        r = requests.get(baseUrl,headers=headers)
        r.encoding = 'utf-8'
        content = BeautifulSoup(r.text,"html.parser")
        return content
    
def createDF(keyword='Python',location='全国'):
    col_names =  ['title', 'jobDescrib', 'companyName','companyIndustry','companyType','companyScal','companyTage','companyLocation','jobUrl']
    df = pd.DataFrame(columns = col_names)
    path = './'+keyword+location+'.csv'
    df.to_csv(path_or_buf = path,encoding='GBK')
    
    return path
    
def saveJob(jobUrl,path):
    colNames =  ['title','jobDescrib','companyName','companyIndustry','companyType','companyScal','companyTage','companyLocation','jobUrl'] 
    df = pd.DataFrame(columns = colNames)
    dic = {}
    
    soup = getSoup(jobUrl)
    
    title = soup.find(class_='new_job_name').get('title')
    jobDescrib = soup.find(class_='job_detail').text.replace('\n',' ').replace('\t',' ')
    jobDescrib = re.sub(' +',' ',jobDescrib)
    companyName = soup.find(class_='com-name').text.replace('\n','')
    
    compDatil = list(soup.find(class_='com-detail').children)
    
    companyIndustry = compDatil[1].text.replace('\n','').replace('/',' ')
    companyType = compDatil[3].text
    companyScal = compDatil[5].text.replace('\n','')
    companyTage = soup.find(class_='com-tags').text.replace('\n',' ')
    companyLocation = compDatil[7].text.replace('\n','')
    
    
    dic['title'] = title
    dic['jobDescrib'] = jobDescrib 
    dic['companyName'] = companyName
    dic['companyIndustry'] = companyIndustry
    dic['companyType'] = companyType
    dic['companyScal'] = companyScal
    dic['companyTage'] = companyTage
    dic['companyLocation'] = companyLocation
    dic['jobUrl'] = jobUrl
        
    df = df.append(dic,ignore_index=True)
    
    
    try:
        df.to_csv(path_or_buf = path, mode="a+", header=None, index=None, encoding="GB18030")
    except Exception as e:
        print(e)
        print('写入失败')
        
    def getJobFromPage(soup):
        if not soup: return []
        jobList = []
        allJob = soup.find_all(class_=['intern-wrap intern-item','intern-wrap intern-item is-view'])
        print(allJob)
#        for job in allJob:             
#            jobList.append(job.find(class_='title ellipsis font').get('href'))
#        return jobList
    
if __name__ == "__main__":
    
#    url = 'https://www.shixiseng.com/interns?page=1&keyword=%E7%88%AC%E8%99%AB&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%8C%97%E4%BA%AC&internExtend='
    url = 'https://www.shixiseng.com/interns?keyword=%E7%88%AC%E8%99%AB&city=%E5%8C%97%E4%BA%AC&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=&publishTime=&sortType=&internExtend=&page=2'
    soup = getSoup(url)
    jobList = getJobFromPage(soup)
    
    print(len(jobList))
    
    
    
    