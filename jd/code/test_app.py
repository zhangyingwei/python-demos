#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: test_app.py 
@time: 2017/11/15 16:02 
"""
import time,datetime

# data = "2015-01-01 00:00:41.0"
data = "2015-01-01 00-01:41.0"
a = time.strptime(data.split(".")[0],"%Y-%m-%d %H-%M:%S")
a = datetime.datetime(a.tm_year,a.tm_mon,a.tm_mday,a.tm_hour,a.tm_min,a.tm_sec)

print(a)
