# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   run
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""
from scrapy import cmdline

cmdline.execute("scrapy crawl rds_Jobs".split())
