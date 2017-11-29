#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: naivebayes.py 
@time: 2017/11/29 16:40
@desc: 朴素贝叶斯分类器
"""

class NaiveBayes:

    def __init__(self,data_set = None):
        self.data_set = data_set
