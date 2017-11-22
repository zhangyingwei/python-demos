#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: knn_nums_app.py 
@time: 2017/11/22 17:43 
"""

from sklearn import datasets
from sklearn.cross_validation import train_test_split
import ml.classify.knn.knn as knn

digits = datasets.load_digits()
datas = digits.data
targets = digits.target

x_train,x_test,y_train,y_test = train_test_split(datas,targets,test_size=0.4)

model = knn.Knn()
model.fit(x_train,y_train)

err = 0
for index,item in enumerate(x_test):
    res = model.predict(item)
    if y_test[index] != res:
        err+=1
        print("实际是{0},识别结果是{1}".format(y_test[index],res))
print(1-err/len(x_test))