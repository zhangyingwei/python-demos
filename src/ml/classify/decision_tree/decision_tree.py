#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: decision_tree.py 
@time: 2017/11/23 14:25 
"""
from collections import Counter
import numpy as np
from math import log


class DecisionTree():

    def __init__(self):
        pass

    def get_shanno_entropy(self,values):
        '''计算熵'''
        val_dict = {}
        print(values)
        for item in values:
            item = str(item)
            if item not in val_dict:
                val_dict[item] = 0
            val_dict[item] += 1
        print(val_dict)
        val_counts = val_dict.values()
        pre_val_count = [v / len(values) for v in val_counts]
        log_val = [v * np.log2(v) for v in pre_val_count]
        return -np.sum(log_val)

    def split_dataset(dataset, classes, feat_idx):
        ''' 根据某个特征以及特征值划分数据集
        :param dataset: 待划分的数据集, 有数据向量组成的列表.
        :param classes: 数据集对应的类型, 与数据集有相同的长度
        :param feat_idx: 特征在特征向量中的索引
        :param splited_dict: 保存分割后数据的字典 特征值: [子数据集, 子类型列表]
        '''
        splited_dict = {}
        for data_vect, cls in zip(dataset, classes):
            feat_val = data_vect[feat_idx]
            sub_dataset, sub_classes = splited_dict.setdefault(feat_val, [[], []])
            sub_dataset.append(data_vect[: feat_idx] + data_vect[feat_idx + 1:])
            sub_classes.append(cls)
        return splited_dict


    def create_tree(self,data_set,classes,feat_names):
        '''
        根据当前数据集递归创建决策树
        :param data_set: 数据集
        :param classes: 数据集中数据相应的特征名称
        :param feat_names: 数据集中数据相应的类型
        :return: tree 以字典形式返回决策树
        '''

        # 如果数据集中只有一种类型，停止分裂，直接返回类型
        if len(set(classes)) == 1:
            return classes[0]

        # 如果遍历完所有特征，返回比例最多的类型
        if len(feat_names) == 0:
            return self.get_majority(classes)

        # 分裂创建新的子树
        tree = {}
        base_feat_idx = self.chose_best_split_feature(data_set,classes)


    def get_majority(self, classes):
        '''
        返回类型中占据大多数的类型
        :param classes:
        :return:
        '''
        class_counts = Counter(classes)
        values = list(class_counts.values())
        args = np.argsort(values)
        return list(class_counts.keys())[args[-1]]

    def chose_best_split_feature(self, data_set, classes):
        '''
        根据信息增益 确定最好的划分数据的特征
        :param data_set: 待划分数据集
        :param classes: 数据集对应的类型
        :return: 确定的最好的特征属性的索引
        '''

        base_entropy = self.get_shanno_entropy(classes)


