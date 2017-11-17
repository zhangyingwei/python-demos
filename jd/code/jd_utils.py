#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: utils.py 
@time: 2017/11/14 17:03 
"""
import os
import sys

import datetime

import numpy
import pandas as pd
import time


class env:
    data_path = "D:/work/code/zhangyingwei/python/python-demos/jd/data"

class Files:
    """
    文件
    """
    type_traid = "traid"
    type_test = "test"
    login = "t_login.csv"
    login_test = "t_login_test.csv"
    trade = "t_trade.csv"
    trade_test = "t_trade_test.csv"


# 读取文件
def read_csv(file_type):
    login_path = ""
    trade_path = ""
    if file_type is Files.type_traid:
        login_path = Files.login
        trade_path = Files.trade
    elif file_type is Files.type_test:
        login_path = Files.login_test
        trade_path = Files.trade_test
    login_path = os.path.join(env.data_path,login_path)
    trade_path = os.path.join(env.data_path,trade_path)

    login_table = pd.read_csv(login_path)
    trade_table = pd.read_csv(trade_path)
    return login_table,trade_table

# 连接表并清洗数据列
def formate_is_scan(is_scan):
    result = []
    for item in is_scan:
        if item == True:
            result.append(0)
        elif item == False:
            result.append(1)
    return result

def formate_time(time_data):
    time_data = str(time_data).split(".")[0]
    time_data = time.strptime(time_data, "%Y-%m-%d %H:%M:%S")
    itemTime = datetime.datetime(time_data.tm_year, time_data.tm_mon, time_data.tm_mday, time_data.tm_hour, time_data.tm_min,time_data.tm_sec)
    biaogTime = datetime.datetime(time_data.tm_year, time_data.tm_mon, time_data.tm_mday, 0, 0, 0)
    return (itemTime - biaogTime).seconds

def formate_times(times):
    result = []
    for time_data in times:
        result.append(formate_time(time_data))
    return result

def formate_tables(login_table,trade_table):
    result_table = trade_table.join(login_table,on="id",how="left",lsuffix="_")
    result_table = result_table.drop(["id","id_","rowkey","log_id"],axis=1)
    # time_
    time_ = result_table.pop("time_")
    result_table.insert(0,"jytime",time_)
    # is_scan
    is_scan = result_table.pop("is_scan")
    is_scan = formate_is_scan(is_scan)
    result_table.insert(0,"is_scan",is_scan)
    # is_sec
    is_sec = result_table.pop("is_sec")
    is_sec = formate_is_scan(is_sec)
    result_table.insert(0,"is_sec",is_sec)
    # all time
    jytime = result_table.pop("jytime")
    jytime = formate_times(jytime)
    result_table.insert(0,"jytime",jytime)

    time_col = result_table.pop("time")
    time_col = formate_times(time_col)
    result_table.insert(0,"login_time",time_col)

    # timestamp = result_table.pop("timestamp")
    # timestamp = [stamp/1000 for stamp in timestamp]
    # result_table.insert(8, "timestamp", timestamp)

    return result_table


def bulid_data(result_table):
    labels = result_table.pop("is_risk")
    return result_table,labels

def save_data(result_table,labels,name=""):
    result_table = numpy.array(result_table.values)
    labels = numpy.array(labels.values)
    with open(os.path.join(env.data_path,"result_table"+name+".npy"),"wb") as result_file:
        numpy.save(result_file,result_table)

    with open(os.path.join(env.data_path,"labels"+name+".npy"),"wb") as labels_file:
        numpy.save(labels_file,labels)

def read_data(name=""):
    with open(os.path.join(env.data_path,"result_table"+name+".npy"),"rb") as result_file:
        result_table = numpy.load(result_file)
    with open(os.path.join(env.data_path,"labels"+name+".npy"),"rb") as labels_file:
        labels_table = numpy.load(labels_file)
    return result_table,labels_table
