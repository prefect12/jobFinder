# 岗位分析
根据关键字抓取对应岗位信息

根据岗位描述找到某岗位所需的条件

## 开始

打开run.py,可以直接运行


## 数据下载
```
from sxc import SXCCrawer  
from processor import SXSAnalyser

cra = SXCCrawer()

#调用参数助手
cra.HELP()

#设置城市和关键字参数
city = ['武汉','北京']
cra.setParams(keyword='算法',city=city)

#开始下载,csv文件会保存在根目录
cra.run()

```


## 数据分析

```
ana = SXSAnalyser(path ='./算法intern全国45.csv')

#minCount，词频阈值，低于数字的就不会被统计，默认10
#select, 绘图词数值，默认100

ana.prapaerData(select=,minCount=)

#图片会自动保存在目录的./image/
#绘制词云图
ana.drawCloud()

#绘制2D类聚词向量图
#ana.draw2D()

#绘制柱状图
ana.drawBar()
```


###词云图
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45wordCloud.jpg)
（点击图片查看大图）<br>
<br>
<br>


###排名靠前的关键字
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45BarChart.jpg)
（点击图片查看大图）<br>
<br>
<br>


###2D关键字之间的关系
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD452D.jpg)
（点击图片查看大图）
<br>
<br>


###3D关键字之间的关系
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD452D.jpg)
（点击图片查看大图）
