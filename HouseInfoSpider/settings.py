# -*- coding: utf-8 -*-

BOT_NAME = 'HouseInfoSpider'

SPIDER_MODULES = ['HouseInfoSpider.spiders']
NEWSPIDER_MODULE = 'HouseInfoSpider.spiders'


#配置
COOKIES_ENABLED = False  #禁止COOKIES
RETRY_ENABLED = False   #禁止重试
DOWNLOAD_TIMEOUT = 15

DOWNLOAD_DELAY = 0.25


#MONGO_DB
MONGO_URI = 'mongodb://127.0.0.1:27017'
MONGO_DATABASE = 'HouseInfo'


#改变默认PIPELNES
ITEM_PIPELINES = {
   'HouseInfoSpider.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#改变user-agent头
DOWNLOADER_MIDDLEWARES = {
      'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
       'HouseInfoSpider.spiders.rotate_useragent.RotateUserAgentMiddleware' : 400,
}


COMMANDS_MODULE = 'HouseInfoSpider.commands'

#redis
SCHEDULER = "HouseInfoSpider.scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'HouseInfoSpider.scrapy_redis.queue.SpiderPriorityQueue'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIE_URL = None


# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0



