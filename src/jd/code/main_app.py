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
import pandas as pd
import jd_utils as utils
import numpy
import time
import datetime

class Data:
    """
    数据
    """
    t_login= "t_login.csv"
    t_login_test= "t_login_test.csv"
    t_trade= "t_trade.csv"
    t_trade_test= "t_trade_test.csv"

    def __init__(self,fileType):
        login,trade = self.getFileName(fileType)
        self.pathLogin = utils.env.data_path+"/"+login
        self.pathTrade = utils.env.data_path+"/"+trade

    def loadCSV(self):
        print("loadCsv")
        loginTable = pd.read_csv(self.pathLogin)
        tradeTable = pd.read_csv(self.pathTrade)
        index_login = loginTable.set_index("id")
        index_trade = tradeTable.set_index("id")
        result = pd.concat([index_login,index_trade],axis=1,join="outer")
        return result

    def loadData(self):
        login,test = self.loadCSV()

        print("bulid loginMap")
        loginMap = {}
        for item in login:
            loginMap[item[9]] = item

        print("append item")
        tmpResult = []
        for testItem in test:
            testItem = [i for i in testItem]
            key = testItem[2]
            appendItem = loginMap.get(key,[])
            appendItem = [i for i in appendItem]
            testItem.remove(key)
            temp = testItem + appendItem
            tmpResult.append(temp)

        """数据清洗"""
        result = []
        for item in tmpResult:
            if len(item)> 5:
                result.append(item)
        return numpy.array(result)

    def getFileName(self, fileType):
        if fileType is "login":
            return Data.t_login,Data.t_trade
        elif fileType is "test":
            return Data.t_login_test,Data.t_trade_test

def initData(table):
    """
    初始化数据，分割成 label 与 data
    :param table:
    :return:
    """
    labels = []
    datas = []
    for item in table:
        labels.append(item[2])
        """
        交易时间
        登录时间
        设备标识
        登录来源
        登录IP
        登录IP归属地
        登录结果
        登录时间戳
        登录类型
        是否扫码登录
        是否使用安全控件
        登录时间
        """
        datas.append([item[1],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[13],item[14],item[15]])
    return labels,formateData(datas)

def formateData(data):
    """
    格式化数据
    :param data:
    :return:
    """
    result = []
    for item in data:
        for index,x in enumerate(item):
            if x == 'True':
                result.append(0)
            elif x == 'False':
                result.append(1)
            elif index == 0:
                result.append(formateTime(x))
            else:
                result.append(x)
    return result

def formateTime(timeData):
    timeData = timeData.split(".")[0]
    timeData= time.strptime(timeData, "%Y-%m-%d %H:%M:%S")
    itemTime = datetime.datetime(timeData.tm_year, timeData.tm_mon, timeData.tm_mday, timeData.tm_hour, timeData.tm_min, timeData.tm_sec)
    biaogTime = datetime.datetime(timeData.tm_year, timeData.tm_mon, timeData.tm_mday, 0, 0, 0)
    return (itemTime-biaogTime).seconds


if __name__ == '__main__':
    table = Data("login").loadCSV()
    print(table)
    # # table = Data("test").loadData()
    # labels,datas = initData(table)
    # print(labels)
    # print(datas)