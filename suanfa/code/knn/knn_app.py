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

import knn

x = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [-1,0,1]
]
y = ['a','b','c','a']
_x = [1,2,3]

model = knn.Knn()
model.fit(x,y)
model.say()
model.predict(_x)
