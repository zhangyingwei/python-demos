#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: file_demos.py 
@time: 2017/11/30 15:23 
"""

import gzip
import pickle

fp = gzip.open("D:/work/code/zhangyingwei/python/python-demos/input/demos/zipfile/mnist.pkl.gz")
a = pickle.load(fp)
print(a)