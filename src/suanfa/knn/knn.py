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
import numpy as np


class Knn:
    def __init__(self):
        pass

    def fit(self,x,y):
        self.x = x
        self.y = y
        self.do_study()

    def predict(self,x):
        data_arr = np.array(x)
        items = self.x
        x_arr = np.array(items)
        # 先求平方差 a方-b方
        result = x_arr*x_arr - data_arr*data_arr
        # 求和 
        result = np.sum(result,axis=1)
        result = np.abs(result)
        result = result**0.5
        index_sort = np.argsort(result)
        return self.y[index_sort[0]]

    def say(self):
        print("hello sb",self.dic)

    def do_study(self):
        dic = {}
        for index,item in enumerate(self.x):
            key = self.y[index]
            dic[str(item)] = key
        self.dic = dic


def hello():
    print("hello hah")