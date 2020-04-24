# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:52:44 2020

@author: Administrator
"""

from sxc import SXCCrawer  
from processor import SXSAnalyser

cra = SXCCrawer()

#调用参数助手
cra.HELP()

#设置参数，开始爬取
city = ['武汉','北京']
cra.setParams(keyword='算法',city=city)
cra.run()

#获取路径
ana = SXSAnalyser(path ='./算法intern全国45.csv')

ana.draw2D()