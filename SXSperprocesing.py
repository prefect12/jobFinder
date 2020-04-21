# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:11:02 2020

@author: Administrator
"""
#encoding=utf-8

import pandas as pd
import numpy as np
import jieba
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import re
from gensim.models import Word2Vec
from sklearn.decomposition import PCA


from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('./算法intern北京23.csv',engine='python')
jieba.load_userdict('./dict.txt')
stopWord = np.array(pd.read_csv('./stopwords/sum.txt',header=None)).T.tolist()[0]


#数据去重
df.dropna(subset=['jobUrl'],inplace=True)
df.fillna(value='',inplace=True)
df.drop_duplicates(['title','companyName','jobDescrib'],inplace = True)
df.index = range(len(df))

#预处理，删除 stop words
df['jobDescrib'] = df['jobDescrib'].apply(lambda x:re.sub('�0|�1|�6|�2|[【】◆]','',x.lower()))
df['title'] = df['title'].apply(lambda x:re.sub('�0|�1|�6|�2|[【】◆]','',x.lower()))
df['titleWord'] = df['title'].apply(lambda x:[i for i in jieba.lcut(x) if len(i)>=2 ])
df['jobDesWord'] = df['jobDescrib'].apply(lambda x:[i for i in jieba.lcut(x) if len(i)>=2 and i not in stopWord])


# 计算词频
wordDf = pd.DataFrame({'Word':np.concatenate(df.jobDesWord)})
wordStat = wordDf.groupby(by=['Word'])["Word"].agg({'number':np.size})
wordStat = wordStat.reset_index().sort_values(by='number',ascending=False)

#根据数字选择
wordStat2 = wordStat.loc[wordStat['number'] >= 10]

#选择前200个
wordStat3 = wordStat.head(200)



#关键词
wordsList = np.array(df.jobDesWord).T.tolist()

model = Word2Vec(wordsList,min_count=1)
X = model[model.wv.vocab]

pac = PCA(n_components=2)
result = pac.fit_transform(X)

words = list(model.wv.vocab)
for i,word in enumerate(words):
    plt.scatter(result[i,0],result[i,1])
    plt.annotate(word,xy=(result[i,0],result[i,1]))
plt.show()



