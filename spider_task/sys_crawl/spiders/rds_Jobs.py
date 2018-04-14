# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   rds_Jobs
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""
import pickle

from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str

from sys_crawl.middles.items import JobItems


class sys_rdsTask(RedisSpider):
    name = 'rds_Jobs'
    redis_key = 'spider:task'

    def __init__(self, *args, **kwargs):
        super(sys_rdsTask, self).__init__(*args, **kwargs)

    def make_request_from_data(self, data):
        '''
                2018-4-14 玖天修改为可以发送request 的任务到redis
        '''
        try:
            req = pickle.loads(data)
            if isinstance(req, Request):
                return req
        except:
            {}
        url = bytes_to_str(data, self.redis_encoding)
        return self.make_requests_from_url(url)

    def parse(self, response):
        jobs = JobItems()
        jobs["url"] = response.request.url  # 需要爬取的url列表
        jobs["body"] = response.body  # response 服务器返回的数据结果
        jobs["meta"] = response.request.meta  # 任务的备注信息 { ... }
        yield jobs