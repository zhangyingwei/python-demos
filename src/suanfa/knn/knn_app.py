#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: test.py 
@time: 2017/11/17 17:00 
"""

import suanfa.knn.knn as knn
from sklearn import datasets
from sklearn.cross_validation import train_test_split

def test1():
    x = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [-1,0,1]
    ]
    y = ['a','b','c','a']
    _x = [-2,1,0]

    model = knn.Knn()
    model.fit(x,y)
    model.say()
    min = model.predict(_x)
    print(min)

def test2():
    iris = datasets.load_iris()
    data = iris.data
    target = iris.target

    x_train,x_test,y_train,y_test = train_test_split(data,target,test_size=0.2)

    model = knn.Knn()
    model.fit(x_train,y_train)
    succ = 0
    err = 0
    for index,item in enumerate(x_test):
        res = model.predict(item)
        tt = y_test[index]
        if res == tt:
            succ += 1
        else:
            err += 1
    print(succ/(succ+err))

test2()