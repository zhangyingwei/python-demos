#!/usr/bin/env python
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: keran_app.py 
@time: 2017/11/27 10:46 
"""

from keras import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation
from keras.layers.embeddings import Embedding

def bulid_model(max_features,maxlen):
    model = Sequential()
    model.add(Embedding(max_features,128,input_length=maxlen))
    model.add(LSTM(128))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation("sigmoid"))
    model.compile(loss="binary_crossentrop",optimizer="rmsprop")
    return model

bulid_model(100,100)