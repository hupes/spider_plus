# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   pipelines
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""

from scrapy.utils.misc import load_object
from scrapy_redis.pipelines import RedisPipeline
from twisted.internet.threads import deferToThread


class jtPipelines(RedisPipeline):

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        try:
            TEMP_PATH = item['meta']['jobs']['TEMP_PATH']
            self.instance = load_object(TEMP_PATH)
            self.instance.run(item)

            rdskey = TEMP_PATH[TEMP_PATH.rindex('.'):]
            self.server.incr("rds_ok:" + rdskey)
        except Exception as e:
            print("解析package路径不正确")
        return item