# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:11:02 2020

@author: Administrator
"""

import pandas as pd
import numpy as np
import pkuseg
import jieba
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv('./算法intern北京23.csv',engine='python')
df = df.fillna(value='')
df.index = range(len(df))

#数据去重
df.drop_duplicates(['title','companyName'],inplace = True)

#岗位名统计
def repIcon(iconString):
    iconString = iconString.replace('�6�1','').replace('�0�2','').replace('�0�1','')
    return iconString

df['title'].value_counts()
df['title'] = df['title'].apply(lambda x:x.lower())
df['jobDescrib'] = df['jobDescrib'].apply(repIcon)

s1 = ' 岗位职责： 1.负责编译工具链的开发与维护； 2.设计或改进编译优化算法，提升编译器优化效能； 3.负责操作系统、编译器以及SDK等软件开发和移植； 4.负责操作系统核心机制的优化； 5.开展面向定制芯片的应用程序编写和测试； 6.负责基于团队SOC芯片中外设模块的驱动开发和相关的软件验证与测试工作； 7.负责目标平台的测试与应用级算法设计、移植与开发； 8.人工智能算法设计及硬件的适配。 岗位要求： 1.微电子、计算机、通信工程、电子信息工程、软件工程类相关专业本科以上学历； 2.有良好的数据结构和算法功底； 3.熟悉汇编语言或者C/C++，有很好的计算机编程语言能力； 4.具有良好的计算机体系结构或者人工智能与深度学习理论基础； 5.熟练使用Linux；有编译器、操作系统开发经验者优先； 6.熟悉TensorFlow等深度学习框架，或者熟悉主流嵌入式操作系统的编译、裁剪、移植及其驱动和应用程序开发； 7.良好的沟通能力和团队协作能力，工作积极主动；'
s2 = '  岗位职责： 1、深入行业研究和企业研究，掌握行业动态及变化规律，掌握企业研究方法及核心关注点，结合数量化工具，为智能投研提出建议； 2、熟悉人工智能前沿领域，掌握机器学习和深度学习最新技术、思想，运用算法解决实践问题，在相关领域有独立研发经验者优先。 任职要求： 1、硕士及以上学历，理工科+金融复合背景优先，2021年应届毕业生； 2、具有严密的逻辑思维能力、数学推导能力和编程能力，学习能力强，踏实勤奋，抗压能力强，具备良好的团队协作能力及沟通理解能力。 '
s3 = ' [实习生]中科院软件所 智能网络安全研究 研究方向： 网络流量安全分析、网络攻防对抗、机器学习、知识图谱等 岗位职责： 网络流量分析、入侵检测、机器学习等研究方向最新前沿论文研读，原型系统实现，网络安全技术改进及创新 任职要求：              1、在校本科及以上，计算机或信息安全方向 2、有较好的网络安全基础和流量分析基础 3、熟悉python编程语言和Linux系统，熟练编写shell脚本 4、熟悉wireshark、Snort等流量分析工具 5、能快速阅读并理解英文论文内容   待遇： 2k-5k，根据个人综合能力确定  为表现优秀者提供留所工作的机会 '

mylist = [s1,s2,s3]
wordList = [" ".join(jieba.cut(s)) for s in mylist]
mytext = ' '.join(wordList)

wordcloud= WordCloud(font_path='simhei.ttf',background_color='black').generate(mytext)
plt.imshow(wordcloud)
plt.axes('off')

plt.show()



#text = jieba.cut(' 【岗位职责】 1、NLP、图像相关工作的调研和落地； 2、处理实际业务数据并解决具体业务问题； 3、主要编程语言为Python／Java。 【任职要求】 1、计算机/数学相关专业，研究生及以上，每周至少实习4天, 实习期至少6个月； 2、有机器学习、数据挖掘、计算机视觉与图像处理、语音识别与合成、自然语言处理等至少一个方向相关基础，有相关项目经验者优先； 3、有较强的逻辑思维，理解力，学习能力； 4、编程基础扎实，熟悉常用算法与数据结构，至少熟悉一门编程语言并有开发经验，如C++. Java. Scala. Python等； 5、了解海量数据处理技术，有使用Hadoop、Hive、Spark等大数据平台分析海量数据的能力和经验者优先； 6、有推荐系统/NLP/深度学习方面经验优先； 7、在计算机相关领域会议/期刊发表过论文者优先。 ')
#text = [i for i in text if len(i) > 2]
#print(Counter(text).most_common(10))
#print(','.join(jieba.cut('我们中出了一个叛徒')))

