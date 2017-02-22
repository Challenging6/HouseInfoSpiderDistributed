# 房屋信息爬虫
基于Scrapy-Redis框架的分布式爬虫
## 信息来源
[中房网](http://www.fangchan.com/)<br>
[房天下](http://wuhan.fang.com/)<br>
[安居客](http://wuhan.anjuke.com)<br>
## 数据格式
`经纬度`、`小区名`、`小区位置`、`房屋面积`、`朝向`、`装修程度`、`楼层`、<br>
`户型`、`单价`、`首付`、`住宅类型`、`总价`、`标题`、`房屋描述`、`月供`<br>

## 主要运行环境
* Windows7及以上
* Python27
* Scrapy1.2及以上+Scrapy-redis
* bs4
* mongodb+redis client

## 运行准备
* 启动Mongodb服务
* 启动Redis服务
* 启动lpush.py
* 启动crawlall.py

## 注意
    
