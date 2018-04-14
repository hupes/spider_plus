# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   RotateUserAgentMiddleware
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""

from sys_crawl.proxyUtls import mayi_Proxy

'''
1. logging.CRITICAL - for critical errors (highest severity) 致命错误
2. logging.ERROR - for regular errors 一般错误
3. logging.WARNING - for warning messages 警告＋错误
4. logging.INFO - for informational messages 消息＋警告＋错误
5. logging.DEBUG - for debugging messages (lowest severity) 低级别
'''




class RequestMiddle(object):
    # def __init__(self):
    #     pass
    # self.mianFeilProxy = IpUtils()
    # self.proxyId = ""
    # self.ipUtils = zm_Proxy()

    # 设置代理
    def setting_spider_random_request_Proxy(self, request):

        authHeader, my_proxy = mayi_Proxy.generate_sign()  # 使用蚂蚁代理
        request.headers.setdefault('Proxy-Authorization', authHeader)
        request.meta['proxy'] = my_proxy

        # self.proxyId = self.ipUtils.getProxyId(self.proxyId)
        # if str(self.proxyId).__eq__("null"):
        #     self.logger.info("付费代理已经使用完了，开始使用免费代理！")
        #     self.proxyId = self.mianFeilProxy.getProxyIp()
        #
        # request.meta['proxy'] = "http://" + str(self.proxyId)
        # log_proxy = "    this spider request proxy:", request.meta['proxy'], "     "
        # self.logger.info(log_proxy)
        # print log_proxy
        pass

    # 判断是否使用代理
    def isProxy(self, request):
        try:
            isproxy = request.meta['jobs']["isproxy"]
            if isproxy:
                self.setting_spider_random_request_Proxy(request=request)
        except Exception as ex:
            print ("Exception_isProxy:", ex.message)
            # 重写scrapy 框架的 process_request 方法

    def process_request(self, request, spider):
        self.isProxy(request)
        pass

    '''
        what happens if request Exception 
        the...again...start...request!
    '''

    def process_exception(self, request, exception, spider):
        print ("exception\t %s"%exception)
        self.isProxy(request)
        return request

    def spider_closed(self, spider, reason):
        print ("close dirver....")
