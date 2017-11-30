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

base_path = "D:/work/code/zhangyingwei/python/python-demos/src/datasets"
data_dic = {
    "KDD99" : [
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
    "SEA":[
        "http://schonlau.net/masquerade/masquerade-data.zip",
        "http://schonlau.net/masquerade/MasqueradeDat.gz",
        "http://schonlau.net/masquerade/masquerade_summary.txt",
        "http://schonlau.net/masquerade/IntrusionMethodScoresAndThresholds.ZIP",
        "http://schonlau.net/masquerade/roc.txt",
        "http://schonlau.net/masquerade/FiguresStatisticalSciencePaper.ZIP",
        "http://schonlau.net/"
    ],
    "ADFA-LD":[],
    "ALEXA":[],
    "MINST":[
        "http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz"
    ],
    "MOVIE-REVIEW-DATA":{
        "Sentiment-polarity-datasets":[
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/polarity_html.zip",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_cleaned.zip",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens_0211.tar.gz",
            "http://www.avaquest.com/about-nate.html",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/mix20_rand700_tokens.zip",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/polarity_html.zip"
        ],
        "Sentiment-scale-datasets":[
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/scale_data.tar.gz",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/scale_whole_review.tar.gz"
        ],
        "Subjectivity-datasets":[
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/rotten_imdb.tar.gz",
            "http://www.cs.cornell.edu/people/pabo/movie-review-data/subjectivity_html.tar.gz"
        ]
    },
    "ENRON":[
        "http://www.aueb.gr/users/ion/data/enron-spam/readme.txt",
        {
            "Enron-Spam-in-pre-processed-form":[
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz",
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron2.tar.gz",
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron3.tar.gz",
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron4.tar.gz",
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron5.tar.gz",
                "http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron6.tar.gz"
            ],
            "Enron-Spam-in-raw-form":{
                "ham-messages":[
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/beck-s.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/farmer-d.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/kaminski-v.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/kitchen-l.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/lokay-m.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/ham/williams-w3.tar.gz"
                ],
                "spam-messages":[
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/spam/BG.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/spam/GP.tar.gz",
                    "http://www.aueb.gr/users/ion/data/enron-spam/raw/spam/SH.tar.gz"
                ]
            }
        }
    ]
}

def download(data_dict,names=[]):
    for item in data_dict.items():
        if type(item) is dict:
            download(item,names)
        else:
            name = item[0]
            paths = item[1]
            names.append(name)
            curr_path = base_path+"/"+"/".join(names)
            if not os.path.exists(curr_path):
                os.makedirs(curr_path)
            for path in paths:
                if type(path) is dict:
                    download(path,names)
                else:
                    print(curr_path)
                    print("get {}-{}".format(name,path))
                    os.system("wget -P "+curr_path+" "+path)
            names.remove(name)

download(data_dic)