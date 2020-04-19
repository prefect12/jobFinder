# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:48:40 2020

@author: Kade
Crawler for shixiseng
"""
# -*- coding:utf-8 -*- 

import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

class SXZCrawer:
    
    def __init__(self):
        
        self.params = {
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
        

    def __createDF(self):
        col_names =  ['title', 'jobDescrib', 'companyName','companyIndustry','companyType','companyScal','companyTage','companyLocation','jobUrl']
        df = pd.DataFrame(columns = col_names)
        path = './'+''.join(list(self.params.values()))+'.csv'
        df.to_csv(path_or_buf = path,encoding='GBK',index=False)
        return path
    
    def __saveJob(self,jobUrl,path):
        colNames =  ['title','jobDescrib','companyName','companyIndustry','companyType','companyScal','companyTage','companyLocation','jobUrl'] 
        df = pd.DataFrame(columns = colNames)
        dic = {}
        
        soup = self.__getSoup(jobUrl)
        
        try:
            title = soup.find(class_='new_job_name').get('title')
            jobDescrib = soup.find(class_='job_detail').text.replace('\n',' ').replace('\t',' ')
            jobDescrib = re.sub(' +',' ',jobDescrib)
            companyName = soup.find(class_='com-name').text.replace('\n','')  
            compDatil = list(soup.find(class_='com-detail').children)
            lenght = len(compDatil)
        except Exception as e:
            print(e)
            return
        
        companyIndustry = compDatil[1].text.replace('\n',' ').replace('/',' ') if lenght > 2 else ''
        companyType = compDatil[3].text if lenght > 4 else ''
        companyScal = compDatil[5].text.replace('\n',' ') if lenght > 6 else ''
        companyTage = soup.find(class_='com-tags').text.replace('\n',' ') 
        companyLocation = compDatil[7].text.replace('\n',' ') if lenght > 8 else ''
        
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
            df.to_csv(path_or_buf = path, mode="a+",index=False,header=None,encoding="GB18030")
        except Exception as e:
            print(e)
            print('写入失败')
        print(dic['title'],dic['companyName'])
        time.sleep(0.5)
            
            
    def __getJobFromPage(self,soup):
        if not soup: return []
        jobList = []
        allJob = soup.find_all(class_=['intern-wrap intern-item','intern-wrap intern-item is-view'])
        for job in allJob:
            jobList.append(job.find(class_='title ellipsis font').get('href'))
        return jobList

    def __getUrlList(self):
        
        def getPage():
            pages = self.__soup.find_all(class_='number')
            temp = []
            for i in pages:
                temp.append(i.text)
            return max(map(int,temp))
        
        numPage = getPage()
        print('Number of pages:',numPage)
        
        urlList = []
        for i in range(1,numPage+1):
            tempUrl = self.__getUrl(page=str(i))
            urlList.append(tempUrl) 
        return urlList
        
    def __getUrl(self,page=1):
        baseUrl = 'https://www.shixiseng.com/interns?'
        self.params['page'] = page
        url = baseUrl + urlencode(self.params)
        return url
    
        
    def __getSoup(self,baseUrl):
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
                }
        try:
           r = requests.get(baseUrl,headers=headers)
           r.encoding = 'utf-8'
           content = BeautifulSoup(r.text,"html.parser")
           return content
        except Exception as e:
            return None
            print(e)
        
    
    def run(self):
        url = self.__getUrl()
        self.__soup = self.__getSoup(url)
        self.__urlList = self.__getUrlList()
        
        path = self.__createDF()
        nums = pages = 0
        
        for url in self.__urlList:
            soup = self.__getSoup(url)
            jobList = self.__getJobFromPage(soup)
            for job in jobList:
                nums += 1
                self.__saveJob(job,path)
            pages += 1
            
            print('='*50,'\n','已经抓取%d页资料'%(pages))
        print('你小子抓了%d条数据，等着坐牢吧你。'%(nums))
        self.params.pop('page')
        
if __name__ == "__main__":
    
    a = SXZCrawer()
    a.params['keyword'] = '人事行政'
    a.run()
