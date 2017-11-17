#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: main_app.py 
@time: 2017/11/14 16:50 
"""
import os

import datetime
import numpy
import pandas as pd
import time
from sklearn import svm
import pickle
import jd_utils as utils

# 读文件
login_table,trade_table = utils.read_csv(utils.Files.type_traid)
result_table = utils.formate_tables(login_table=login_table,trade_table=trade_table)
rsult_table,labels = utils.bulid_data(result_table=result_table)
utils.save_data(result_table=result_table,labels=labels,name="-trade")
# 数据 标签
result_table,labels_table = utils.read_data(name="-trade")

def data_fit():
    model = svm.SVC()
    print("fit...")
    model.fit(result_table,labels_table)
    with open(os.path.join(utils.env.data_path,"model.svm"),"wb") as model_file:
        pickle.dump(model,model_file)

data_fit()