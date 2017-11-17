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
# import main_jd_app as app

def load_test_data():
    login_table = pandas.read_csv(os.path.join(utils.env.data_path,"t_login_test.csv"))
    trade_table = pandas.read_csv(os.path.join(utils.env.data_path,"t_trade_test.csv"))

    # result_table = app.formate_tables(login_table,trade_table)
    # return result_table
    pass



def load_model():
    with open(os.path.join(utils.env.data_path,"model.svm"),"rb") as model_file:
        model = pickle.load(model_file)
    return model


if __name__ == '__main__':
    result_table = load_test_data()
    print(result_table)