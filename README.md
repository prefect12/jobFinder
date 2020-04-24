# 实习僧找工作
根据关键字抓取对应岗位信息

根据岗位描述找到某岗位所需的条件

## 开始

打开run.py,安装好依赖库后可以直接运行


```
from sxc import SXCCrawer  
from processor import SXSAnalyser

cra = SXCCrawer()

#调用参数助手
cra.HELP()

#设置城市和关键字参数
city = ['武汉','北京']
cra.setParams(keyword='算法',city=city)

#csv文件会保存在根目录
cra.run()

```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

词云图
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45wordCloud.jpg)
（点击查看大图）



排名靠前的关键字
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD45BarChart.jpg)
（点击查看大图）



关键字之间的关系
![image](https://github.com/prefect12/jobFinder/blob/master/image/%E7%AE%97%E6%B3%95intern%E5%85%A8%E5%9B%BD452D.jpg)
（点击查看大图）
