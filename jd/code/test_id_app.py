#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: test_id_app.py 
@time: 2017/11/16 17:10 
"""
import os
import pickle
import jd_utils as utils
import pandas

def load_test_data():
    login_table = pandas.read_csv(os.path.join(utils.env.data_path,"t_login_test.csv"))
    trade_table = pandas.read_csv(os.path.join(utils.env.data_path,"t_trade_test.csv"))
    print(login_table[:2])
    print(trade_table[:2])
    # result_table = utils.formate_tables(login_table=login_table,trade_table=trade_table)
    result_table = trade_table.join(login_table, on="id", how="left", lsuffix="_")
    print(result_table[:2])
    # for line in result_table.values:
    #     print(line)
    return result_table



def load_model():
    with open(os.path.join(utils.env.data_path,"model.svm"),"rb") as model_file:
        model = pickle.load(model_file)
    return model


if __name__ == '__main__':
    result_table = load_test_data()
    # model = load_model()
    # res = model.predict(result_table.values)
    # print(len(res))