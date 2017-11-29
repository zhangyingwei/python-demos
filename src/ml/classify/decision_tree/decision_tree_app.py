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

from ml.classify.decision_tree.decision_tree import DecisionTree

dataSet = [
    [1, 3, 0, 1, 'no'],
    [1, 3, 0, 2, 'no'],
    [2, 3, 0, 1, 'yes'],
    [3, 2, 0, 1, 'yes'],
    [3, 1, 1, 1, 'yes'],
    [3, 1, 1, 2, 'no'],
    [2, 1, 1, 2, 'yes'],
    [1, 2, 0, 1, 'no'],
    [1, 1, 1, 1, 'yes'],
    [3, 2, 1, 1, 'yes'],
    [1, 2, 1, 2, 'yes'],
    [2, 2, 0, 2, 'yes'],
    [2, 3, 0, 1, 'yes'],
    [3, 2, 0, 2, 'no']
]
labels = ['age','salary','isStudent','credit']

model = DecisionTree()
data_set = [item[0:4] for item in dataSet]
feat_names = labels
classes = [item[4] for item in dataSet]

model.create_tree(data_set,classes,feat_names)

tree_file_name = "decision_tree.pkl"
if os.path.exists(tree_file_name):
    model.load_tree(tree_file_name)
else:
    model.create_tree(data_set,classes,feat_names)
    model.dump_tree(tree_file_name)

data_vect = data_set[8]
res = model.classify(data_vect,feat_names)
print(res)



