from setuptools import setup

setup(
    name='spider_plus',
    version='1.0',
    packages=['spider_task', 'spider_task.sendTask', 'spider_task.sys_crawl', 'spider_task.sys_crawl.middles', 'spider_task.sys_crawl.spiders',
              'spider_task.sys_crawl.proxyUtls', 'spider_task.sys_crawl.templates'],
    url='',
    license='',
    author='jt',
    author_email='hupe_jt@163.com',
    description='scrapy爬虫模板动态加载'
)
