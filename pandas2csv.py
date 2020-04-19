# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:58:04 2020

@author: Administrator
"""
from pandas import DataFrame,Series

import pandas as pd
import os
path = os.getcwd()

title = '运营实习生'	
company = 'qunimade'	 
detail = '招运营实习生 【来做什么】 1.参与骑象小学堂各种用户运营、社群运营工作。 2.参与组织线下线上运营活动及产品运营的其他各项工作中。 3.搭建和运营用户社群，促进用户转化。 【我们对你的期待】 1.靠谱，既然来实习，就把自己当正式员工要求，这样才能学到东西 2.喜欢互联网、喜欢社交，也有点喜欢表现自己 3.熟悉豆瓣、知乎、微博、抖音、B站等平台，爱琢磨别人家运营玩法 4.每周坐班5天，实习期至少3个月 5.如果你愿意，可以在简历里写上自己在各平台的ID和链接 【我们能给你这些】 1、能实操，有老师指导，有转正机会 2. 120元/天实习补贴，有饭补，加班打车报销 3.不打杂、真正参与公司关键业务 4. 活泼有爱的公司氛围，很多实习生离职后会推荐自己的室友、同学也来实习 5 公司坐标上海浦东软件园'
jobUrl = 'https://www.shixiseng.com/intern/inn_ccf97qcnhiyr?pcm=pc_SearchList'

col_names =  ['title', 'company', 'detail', 'jobUrl']

df = pd.DataFrame(columns = col_names)
df.to_csv(path_or_buf = './test.csv',encoding='GBK',index=False)

def getDic(title,company,detail,jobUrl):
    dic = {'title':title,'company':company,'detail':detail,'jobUrl':jobUrl}
    return dic

df = pd.DataFrame(columns = col_names)
df = df.append(getDic(title,company,detail,jobUrl),ignore_index=True)
df.to_csv(path_or_buf = './test.csv',mode='a+',encoding='GBK',index=False,header=None)


df.to_csv(path_or_buf = './test.csv',encoding='GBK')

