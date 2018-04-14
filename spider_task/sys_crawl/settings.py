# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   settings
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""

BOT_NAME = 'sys_crawl'

SPIDER_MODULES = ['sys_crawl.spiders']
NEWSPIDER_MODULE = 'sys_crawl.spiders'
# 这一项，将这里面的内容拷贝就可以。
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'

# 禁止cookies
COOKIES_ENABLED = False
# 反爬机制
ROBOTSTXT_OBEY = False
# 日志的级别
LOG_LEVEL = "INFO"
# 日志文件名称
# LOG_FILE = "C:/Users/hupe/Desktop/spider_task/scrapy_log/sys_spider.log"
# 设置取消禁止重定向
REDIRECT_ENABLED = True
# 开启线程数量，默认16
CONCURRENT_REQUESTS = 20
# 取消默认的useragent,使用新的useragent
# 超时时间
DOWNLOAD_TIMEOUT = 30
FEED_EXPORT_ENCODING = 'utf-8'
# 启用Ajax爬取
AJAXCRAWL_ENABLED = True
HTTPERROR_ALLOWED_CODES = [302]
DOWNLOADER_MIDDLEWARES = {
    # 关闭默认下载器
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None
    # 键为中间件类的路径，值为中间件的顺序
    , 'sys_crawl.middles.RotateUserAgentMiddleware.RotateUserAgent': 100
    , "sys_crawl.middles.RequestByProxyMiddleware.RequestMiddle": 120
}

# ------------scrapy-redis 分布式爬虫相关设置-----------------
# 修改scrapy默认的调度器为scrapy重写的调度器 启动从reids缓存读取队列调度爬虫
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 调度状态持久化，不清理redis缓存，允许暂停/启动爬虫
SCHEDULER_PERSIST = True
# 存储爬取到的item，一定要在所有的pipeline最后，即设定对应的数字大于其他pipeline
ITEM_PIPELINES = {
    'sys_crawl.middles.pipelines.jtPipelines': 300
}

# 也是爬虫第一次启动时的等待时间（应为队列是空的）
SCHEDULER_IDLE_BEFORE_CLOSE = 10
# 请求调度使用优先队列（默认)
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 如果设置了这一项，则程序会有限采用此项设置，忽略REDIS_HOST 和 REDIS_PORT的设置
REDIS_URL = 'redis://root:xxxxx@域名:端口/库'
# ------------end scrapy-redis----------------------------