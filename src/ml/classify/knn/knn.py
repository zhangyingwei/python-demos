#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: knn.py 
@time: 2017/11/17 16:38 
"""
from collections import Counter
import numpy as np


class Knn:
    def __init__(self):
        pass

    def fit(self,x,y):
        self.x = x
        self.y = y
        # self.do_study()

    def predict(self,x,k = 19):
        data_arr = np.array(x)
        items = self.x
        x_arr = np.array(items)
        data_arr = np.tile(data_arr, (x_arr.shape[0], 1))
        diff_arr = x_arr - data_arr # ai-bi
        sqdiff = diff_arr**2 # (ai-bi)平方
        sumdiff = np.sum(sqdiff,axis=1) # 平方和
        result = sumdiff**0.5 # 开方
        # 获取排序后的数据 index(索引) 列表
        args = np.argsort(result)
        # 以下为获取距离最近的前 K 个数据并求出类型最多的数据类型
        values = []
        for index in range(k):
            values.append(self.y[args[index]])
        values_count = Counter(values)
        arg_values = np.argsort(list(values_count.values()))
        # print("values{0},chrose{1}".format(str(values),list(values_count.keys())[arg_values[-1]]))
        return list(values_count.keys())[arg_values[-1]]

def hello():
    print("hello hah")