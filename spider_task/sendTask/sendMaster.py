# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   sendMaster
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""

# -*- coding: utf-8 -*-
import pickle
import base

# 虾皮首页类目数据发布
from pandas.io import json
from scrapy import Request

if __name__ == '__main__':
    meta = {"jobs":
        {
            "TEMP_PATH": 'sys_crawl.templates.master01.test01', "isproxy": True
        }
    }
    req = Request('https://shopee.tw/api/v1/category_list', meta=meta, dont_filter=True)
    # req = Request('https://shopee.tw/api/v1/category_list',  dont_filter=True)

    task_list = []
    for i in range(0, 250):
        task_list.append(pickle.dumps(req))
    base.set_redis(task_list, rds="spider:task")
