#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: get_datasets.py 
@time: 2017/11/30 10:35 
"""
import os
import subprocess


data_dic = {
    "kdd99" : [
        "http://kdd.ics.uci.edu/databases/kddcup99/task.html",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.names",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.testdata.unlabeled_10_percent.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/corrected.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/corrected.gz",
        "http://kdd.ics.uci.edu/databases/kddcup99/typo-correction.txt"
    ],
    "sea":[
        "http://schonlau.net/masquerade/masquerade-data.zip",
        "http://schonlau.net/masquerade/MasqueradeDat.gz",
        "http://schonlau.net/masquerade/masquerade_summary.txt",
        "http://schonlau.net/masquerade/IntrusionMethodScoresAndThresholds.ZIP",
        "http://schonlau.net/masquerade/roc.txt",
        "http://schonlau.net/masquerade/FiguresStatisticalSciencePaper.ZIP",
        "http://schonlau.net/"
    ]
}

for (name,paths) in data_dic.items():
    if not os.path.exists(name):
        os.makedirs(name)
    for path in paths:
        print("get {}-{}".format(name,path))
        subprocess.call("wget",path)