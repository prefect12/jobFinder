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

class SXCCrawer:
    
    def __init__(self):
        self.setParams(keyword='爬虫',area='',months='',days='',degree='',official='',salary='',publishTime='',city=['全国'])

    def HELP(self):
        
        publishDic = {
                'city':'职位发布时间',
                'day':'今天发布',
                'wek':'这周发布',
                'mon':'三十天内发布'
                }
        
        monDic = {
                'mon':'实习时间',
                '1':'一个月',
                '2':'两个月',
                '3':'三个月',
                '4':'三个月以上'
                }
        
        dayDic = {
                'day':'一周工作天数',
                '1':'1天',
                '2':'2天',
                '3':'3天',
                '4':'4天',
                '5':'5天',
                '6':'6天以上'
                }
        
        degreeDic = {
                'degree':'学历要求',
                '大专':'大专',
                '本科':'本科',
                '硕士':'硕士',
                '博士':'博士'
                }
        
        cityDic = {
                'city':'工作城市',
                '例子':'["武汉","北京"]'
                
                }
        
        keyDic = {
                'keyword':'职位关键字',
                '例子':'算法工程师/Python'
                }
        areaDic = {
                'area':'城市区域',
                '例子':'朝阳区'
                }
        
        salaryDic = {
                'salary':'日薪',
                '-0':'不限',
                '0-100':'0-100',
                '100-150':'100-150',
                '150-200':'150-200',
                '200-300':'200-300',
                '300-':'300以上'
                }
        
             
        dicList = [keyDic,cityDic,areaDic,publishDic,monDic,dayDic,degreeDic,salaryDic]
    
        for i in dicList:
            for j in i:
                print(j+':'+i[j])
            print('\n')
        
    def setParams(self,keyword='',area='',months='',days='',degree='',official='',salary='-0',publishTime='',city=''):
        self.__params = {
        'page':0,
        'keyword':'',
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
        'city':'',
        'internExtend':''
        }
        
        self.__validation = {
                'city':[''],
                'keyword':[''],
                'area':[''],
                
                #发布时间
                'publishTime':['day','wek','mon'],
                
                #实习时长1个月，2个月，3个月，三个月以上
                'mon':['1','2','3','4'],
                
                #每周工作天数 1，2，3，4，5，6天以上
                'days':['1','2','3','4','5','6'],
                
                #学历要求
                'degree':['大专','本科','硕士','博士'],
                
                #日薪
                'salary':['-0','0-100','100-150','150-200','200-300','300-']
                }
        
        translation = {
                'keyword':'关键字',
                'city':'城市',
                'publishTime':'发布时间',
                'mon':'实习时常',
                'days':'每周工作天数',
                'degree':'学历',
                'salary':'日薪',
                'area':'区域'
                }
        
        self.__params['keyword'] = keyword
        self.__params['area'] = area
        self.__params['months'] = months
        self.__params['days'] = days
        self.__params['degree'] = degree
        self.__params['official'] = official
        self.__params['salary'] = salary
        self.__params['publishTime'] = publishTime
        self.__params['city'] = city
        
        print('当前抓取参数:')
        
        for i in self.__params:
            if i in self.__validation:
                print(i + ':' + str(self.__params[i]))
        print('\n')

        
    def __createDF(self):
        col_names =  ['title', 'jobDescrib', 'companyName','companyIndustry','companyType','companyScal','companyTage','companyLocation','jobUrl']
        df = pd.DataFrame(columns = col_names)
        self.__params['city'] = self.__cities
        path = './'+''.join([str(i) for i in self.__params.values()])+'.csv'
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

    def __getUrlList(self,soup):
        
        def getPage(soup):
            pages = soup.find_all(class_='number')
            temp = []
            for i in pages:
                temp.append(i.text)
            return max(map(int,temp))
        
        numPage = getPage(soup)
        
        
        urlList = []
        for i in range(1,numPage+1):
            tempUrl = self.__getUrl(page=str(i))
            urlList.append(tempUrl) 
        return urlList
        
    def __getUrl(self,page=1):
        baseUrl = 'https://www.shixiseng.com/interns?'
        self.__params['page'] = page
        url = baseUrl + urlencode(self.__params)
        return url
    
        
    def __getSoup(self,baseUrl):
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'referer': 'https://www.shixiseng.com/interns?page=1&keyword=%E7%88%AC%E8%99%AB&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%8C%97%E4%BA%AC&internExtend='
                }
        try:
           r = requests.get(baseUrl,headers=headers)
           r.encoding = 'utf-8'
           content = BeautifulSoup(r.text,"html.parser")
           return content
        except Exception as e:
            print(e)
            return None
            
            
    def __getAllUrl(self):
        self.__cities = self.__params['city']
        self.__urlList = []
        for city in self.__cities:
            self.__params['city'] = city
            url = self.__getUrl()
            soup = self.__getSoup(url)
            self.__urlList.extend(self.__getUrlList(soup))

    
    def run(self):
        
        self.__getAllUrl()  
        self.path = self.__createDF()
        nums = pages = 0
        
        print('number of page:',len(self.__urlList))
        

        for url in self.__urlList:
            soup = self.__getSoup(url)
            jobList = self.__getJobFromPage(soup)

            for job in jobList:
                nums += 1
                self.__saveJob(job,self.path)
            pages += 1
            
            print('第%d页数据已抓取完毕。'%(pages),'='*50,'\n')
#        print('你小子抓了%d条数据，等着坐牢吧你。'%(nums))
        self.__params.pop('page')
        

if __name__ == "__main__":
    
    a = SXCCrawer()
    a.setParams(keyword='爬虫',city = ['北京','上海','广州','深圳'])
    a.run()
