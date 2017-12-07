#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: naivebayes_app.py 
@time: 2017/11/29 16:40 
"""

import ml.classify.naivebayes.naivebayes as naivebayes

posting_list = [
    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
    ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
]
def create_data_sets():
    # 0 侮辱性文字 1 正常言论
    class_vec = [1,0,0,1,0,1]
    return posting_list,class_vec

def test():
    posting_list,class_vec = create_data_sets()
    model = naivebayes.NaiveBayes()
    model.trainNB(data_set=posting_list,targets=class_vec)
    for item in posting_list:
        res = model.classify(item)
        print("result is {}".format(res))

    res = model.classify(word_list=["you","are","dog","you","are","my","son"])
    print(res)

def test2():
    data_set = [
        "我 操 你妈",
        "你 他妈 傻逼",
        "都 他妈 脑残",
        "楼主 好人",
        "我 妈 特别 喜欢 你的 文章",
        "你妈 喊你 回家 吃饭 了"
    ]
    target = [0,0,0,1,1,1]
    data_set = [item.split(" ") for item in data_set]
    print(data_set)
    model = naivebayes.NaiveBayes()
    model.trainNB(data_set=data_set, targets=target)
    res = model.classify(word_list="你妈 的 你 是 傻逼 吧".split(" "))
    print(res)
    res = model.classify(word_list="楼主 是个 好人 我 特别 喜欢 你".split(" "))
    print(res)

if __name__ == '__main__':
    test2()