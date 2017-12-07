#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: naivebayes.py 
@time: 2017/11/29 16:40
@desc: 朴素贝叶斯分类器
"""
import numpy as np

class NaiveBayes:

    def __init__(self):
        self.__data_set = None # 训练数据集
        self.__list_of_world = None # 去重之后的词集
        self.__targets = None # 样本标签
        self.__vec_set = None
        self.__p0 = 0.0 # 正样本的概率
        self.__p1 = 0.0 # 负样本的概率

    def trainNB(self,data_set = None,targets = None):
        '''
        训练模型
        :param data_set:
        :return:
        '''
        self.__data_set = data_set
        self.__targets = targets
        self.__words = self.__get_list_of_worlds(data_set)

        vec_set = []
        for item in data_set:
            base_word_vec = self.__get_word_vec(item)
            vec_set.append(base_word_vec)
        self.__vec_set = vec_set

        num0 = np.ones(len(self.__words))
        num1 = np.ones(len(self.__words))
        count0 = 2.0
        count1 = 2.0
        for index,item in enumerate(vec_set):
            if targets[index] == 0:
                num0+=item
                count0+=sum(item)
            elif targets[index] == 1:
                num1+=item
                count1 += sum(item)

        self.__p0 = np.log(num0/count0)
        self.__p1 = np.log(num1/count1)

    def classify(self,word_list):
        word_vec = self.__get_word_vec(word_list)
        pbad = sum(self.__targets)/len(self.__targets)
        p0 = sum(word_vec * self.__p0) + np.log(1 - pbad)
        p1 = sum(word_vec * self.__p1) + np.log(pbad)
        # print("p0 is {} and p1 is {}".format(p0,p1))
        if p0 > p1:
            return 0
        else:
            return 1

    def __get_list_of_worlds(self,data_set):
        '''
        构造词集模型
        :param data_set:
        :return:
        '''
        result = set([])
        for item in data_set:
            result = result | set(item)
        return list(result)

    def __get_word_vec(self, item):
        base_word_vec = [0] * len(self.__words)
        for word in item:
            if word in self.__words:
                base_word_vec[self.__words.index(word)] = 1
        return base_word_vec