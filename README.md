# spider_plus
setting 的必要修改项，请注意上传redis 的任务格式，和spider 的解析格式是否一致。redis存储的是Request对象…  …
…而不是url

# 修改scrapy-redis
1. 修改任务发布规则，使redis 不仅仅只能传递url

```Python

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
```

2.配置scrapy.setting
```Python
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
```

3. 找到项目下的 templates文件夹编写的你html解析模板即可

'''Python
#发布任务时，必须带上模板的路径 package.cls
并且你的模板必须得实现 run 方法
```

4。写了这么多只为抛砖引玉，以求共进！~！
