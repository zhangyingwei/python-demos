#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: naivebayes_test.py 
@time: 2017/12/7 14:14 
"""
import os
import jieba
import numpy as np
from ml.classify.naivebayes.naivebayes import NaiveBayes


def load_data(path_wf):
    filenames = os.listdir(path_wf)
    result_list = []
    g_names = []
    for file in filenames:
        file_path = "{}/{}".format(path_wf,file)
        with open(file_path,encoding="UTF-8") as gc:
            lines = gc.readlines()
            g_names.append(lines[0])
            lines = [line.replace("汪峰","") for line in lines]
            lines = [line.replace("郑钧","") for line in lines]
            lines = [list(jieba.cut(line)) for line in lines]
            word_list = list([])
            for line in lines:
                word_list = word_list + list(line)
            word_list = [
                word for word in word_list if word!='\n'
                                              and word != ' '
                                              and word != '：'
                                              and word != ', '
                                              and word != '-'
                                              and word != ', '
                                              and word != ':'
                                              and word != ')'
                                              and word != '('
                                              and word != '《'
                                              and word != '》'
                                              and word != '？'
            ]
            result_list.append(word_list)
    return result_list,g_names


def load_data_set():
    path_wf = "D:/work/code/zhangyingwei/python/python-demos/input/ml/classify/naivebayes/geci/wf"
    path_zj = "D:/work/code/zhangyingwei/python/python-demos/input/ml/classify/naivebayes/geci/zj"

    data_wf,wfg_names = load_data(path_wf)
    data_zj,zjg_names = load_data(path_zj)

    target_wf = [0]*len(data_wf)
    target_zj = [1]*len(data_zj)

    target = target_wf + target_zj
    data_set = data_wf+data_zj
    g_names = wfg_names+zjg_names

    return data_set,target,g_names


if __name__ == '__main__':
    data_set,target,g_names = load_data_set()
    length = len(data_set)

    test_data_size = 2
    test_data = data_set[length-test_data_size:]
    test_target = target[length-test_data_size:]
    test_name = g_names[length-test_data_size:]

    test_data2 = data_set[:test_data_size]
    test_target2 = target[:test_data_size]
    test_name2 = g_names[:test_data_size]

    name_dic = {
        0:"汪峰",
        1:"郑钧"
    }

    model = NaiveBayes()
    model.trainNB(data_set=data_set[test_data_size:length-test_data_size], targets=target[test_data_size:length-test_data_size])
    for index,line in enumerate(test_data):
        res = model.classify(word_list=line)
        print("{} 是 {} 的歌".format(test_name[index].replace("\n",""),name_dic[res]))
        # print("res is {} and should be {}".format(res,test_target[index]))

    for index, line in enumerate(test_data2):
        res = model.classify(word_list=line)
        print("{} 是 {} 的歌".format(test_name2[index].replace("\n",""), name_dic[res]))
        # print("res is {} and should be {}".format(res, test_target2[index]))

