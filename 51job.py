# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:05:01 2020

@author: Administrator
"""

import requests
import pandas as pd
from pprint import pprint
from lxml import etree
import time
import warnings
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re
import pandas as pd


warnings.filterwarnings("ignore")

class Job51Crawer:
    def __init__(self):
        self.setParams(keyword='算法',city=['全国'])
        
        
    def setParams(self,keyword,city):
        self.__params = {
                'keyword':keyword,
                'city':city
                }
        self.path = self.__createDF()

        cityDic = {'全国':'000000','北京': '010000', '上海': '020000', '广州': '030200', '深圳': '040000', '武汉': '180200', '西安': '200200', '杭州': '080200', '南京': '070200', '成都': '090200', '重庆': '060000', '东莞': '030800', '大连': '230300', '沈阳': '230200', '苏州': '070300', '昆明': '250200', '长沙': '190200', '合肥': '150200', '宁波': '080300', '郑州': '170200', '天津': '050000', '青岛': '120300', '济南': '120200', '哈尔滨': '220200', '长春': '240200', '福州': '110200'}
        
        cities = ''
        for c in city:
            cities += cityDic[c] + '%252C'
    
        self.__params['city'] = cities[:-5]
        self.__params['keyword'] = keyword
        
    def __getUrl(self,page=1):
        
        url = 'https://search.51job.com/list/'+self.__params['city']+',000000,0000,00,9,99,'+self.__params['keyword']+',2,'+str(page)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        return url

        
        
    def __createDF(self):
        col_names =  ['title', 'jobDescrib', 'companyName','companyIndustry','companyScal','companyTage','companyLocation','jobUrl','salary','publicDate','degree']
        df = pd.DataFrame(columns = col_names)
        path = './'+''.join([str(i) for i in self.__params.values()])+'.csv'
        df.to_csv(path_or_buf = path,encoding='GBK',index=False)
        return path
    
    
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
    
    def __getSoup(self,baseUrl):
        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
                'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Referer': 'https://www.51job.com/'
                }
        try:
           web = requests.get(baseUrl,headers=headers)
           web.encoding = 'gbk'
#           content = BeautifulSoup(r.text,"html.parser")
           return web
        except Exception as e:
            print(e)
            return None
        
        
    def __saveJob(self,web):
        
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-AU;q=0.8,en;q=0.7',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://www.51job.com/'
        }
        
         # 1、岗位名称

        dom = etree.HTML(web.text)
        job_name = dom.xpath('//div[@class="dw_table"]/div[@class="el"]//p/span/a[@target="_blank"]/@title')
        # 2、公司名称
        company_name = dom.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t2"]/a[@target="_blank"]/@title')
        # 3、工作地点
        address = dom.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t3"]/text()')
        # 4、工资
        salary_mid = dom.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t4"]')
        salary = [i.text for i in salary_mid]
        # 5、发布日期
        release_time = dom.xpath('//div[@class="dw_table"]/div[@class="el"]/span[@class="t5"]/text()')
        # 6、获取二级网址url
        deep_url = dom.xpath('//div[@class="dw_table"]/div[@class="el"]//p/span/a[@target="_blank"]/@href')
        RandomAll = []
        JobDescribe = []
        CompanyType = []
        CompanySize = []
        Industry = []
        for i in range(len(deep_url)):
            print(job_name[i],company_name[i])
            web_test = requests.get(deep_url[i], headers=headers)
            web_test.encoding = "gbk"
            dom_test = etree.HTML(web_test.text)
            # 7、爬取经验、学历信息，先合在一个字段里面，以后再做数据清洗。命名为random_all
            random_all = dom_test.xpath('//div[@class="tHeader tHjob"]//div[@class="cn"]/p[@class="msg ltype"]/text()')
            # 8、岗位描述性息
            job_describe = dom_test.xpath('//div[@class="tBorderTop_box"]//div[@class="bmsg job_msg inbox"]/p/text()')
            # 9、公司类型
            company_type = dom_test.xpath('//div[@class="tCompany_sidebar"]//div[@class="com_tag"]/p[1]/@title')
            # 10、公司规模(人数)
            company_size = dom_test.xpath('//div[@class="tCompany_sidebar"]//div[@class="com_tag"]/p[2]/@title')
            # 11、所属行业(公司)
            industry = dom_test.xpath('//div[@class="tCompany_sidebar"]//div[@class="com_tag"]/p[3]/@title')
            # 将上述信息保存到各自的列表中
            RandomAll.append(random_all)
            JobDescribe.append(job_describe)
            CompanyType.append(company_type)
            CompanySize.append(company_size)
            Industry.append(industry)
            # 为了反爬，设置睡眠时间
            time.sleep(1)
            

        df = pd.DataFrame()
        df['title'] = job_name
        df['jobDescrib'] = JobDescribe
        df['companyName'] = company_name

        df['companyScal'] = CompanySize
        df['companyTage'] = Industry
        df['companyLocation'] = address
        df['jobUrl'] = deep_url
        df['salary'] = salary
        df['publicDate'] = release_time
        df['degree'] = RandomAll
        
        
        # 这里在写出过程中，有可能会写入失败，为了解决这个问题，我们使用异常处理。
        try:
            df.to_csv(self.path, mode="a+", header=None, index=None, encoding="gbk")
            
        except:
            print("当页数据写入失败")
        time.sleep(1)
    
    
    def run(self):
        url = self.__getUrl()
        web = self.__getSoup(url) 
        content = BeautifulSoup(web.text,"html.parser")
        numPages = int(content.find(id='hidTotalPage').get('value'))

        print('一共有%d页面'%(numPages),'\n')

        for page in range(1,numPages):
            
            url = self.__getUrl(page)
            web = self.__getSoup(url)
            self.__saveJob(web)

            print('='*50,'\n%d页已抓取完毕\n'%(page),'='*50)
    
if __name__ == '__main__':
    
    jobCra = Job51Crawer()
