#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: decision_tree_app.py 
@time: 2017/11/22 15:01 
"""
import numpy as np
import os
from ml.classify.decision_tree.trees import DecisionTreeClassifier as DecisionTree
# from ml.classify.decision_tree.decision_tree import DecisionTree
from sklearn import datasets
from sklearn.cross_validation import train_test_split

digits = datasets.load_iris()

model = DecisionTree()
data_set = digits.data
# feat_names = [a for a in range(len(data_set[0]))]
feature_names = digits.feature_names
classes = digits.target

x_train,x_test,y_train,y_test = train_test_split(data_set,classes,test_size=0.4)
x_train = [a for a in x_train]
x_test = [a for a in x_test]
y_train = [a for a in y_train]
y_test = [a for a in y_test]

tree_file_name = "decision_tree_digits.pkl"
if os.path.exists(tree_file_name):
    model.load_tree(tree_file_name)
else:
    model.create_tree(x_train,y_train,feature_names)
    model.dump_tree(tree_file_name)

for x,y in zip(x_test,y_test):
    x = [a for a in x]
    res = model.classify(x,feature_names)
    try:
        print("predict{},res{}".format(res,y))
    except KeyError:
        print("errot{}".format(x))
#
# data_vect = data_set[8]
# res = model.classify(data_vect,feat_names)
# print(res)



