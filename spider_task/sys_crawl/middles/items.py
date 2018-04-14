# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   items
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""

import scrapy


class JobItems(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()  # 需要爬取的url列表
    body = scrapy.Field()  # response 服务器返回的数据结果
    meta = scrapy.Field()  # 任务的备注信息 { ... }
    pass

