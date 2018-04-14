# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     spider_task
   IDE Name:    PyCharm
   File Name:   base
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/4/14
   Description :
-------------------------------------------------
   Change Activity: 2018/4/14:
-------------------------------------------------
"""
import pymysql
import redis

pool = redis.ConnectionPool(host="xxxxxxx", password="xxxxxxx..", port="xxxxxx", db=1)

red = redis.Redis(connection_pool=pool)


# mysql connection

# 写数据到redis
def set_redis(data_list, rds="rds:task05"):
    index = 0
    for item_date in data_list:
        p = red.pipeline()
        p.lpush(rds, item_date)
        # red.lpush(rds, data)

        index = index + 1
        print("input task :%s" % index)
        p.execute()
    print("list 数据:%s" % len(data_list))
    print("写入redis：%s" % index)


config = {
    'host': "localhost",
    'port': 3306,
    'user': "xxxxx",
    'password': "xxxxx..",
    'db': "xxxxx",
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}


def ExcSql(sql):
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # 提交
    conn.commit()
    # 关闭链接
    cursor.close()
    conn.close()
    return result


# 分页查询
'''
sql = sql语句
page_size = 第几页
page_count = 每页显示条
'''


def getSqlPage(sql, page_size, page_count):
    startPage = (page_size - 1) * page_count
    sql = "%s limit %s,%s" % (sql, startPage, page_count)
    return sql

