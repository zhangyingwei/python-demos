#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: knn_nums_app.py 
@time: 2017/11/22 17:43 
"""

from sklearn import datasets
from sklearn.cross_validation import train_test_split
import ml.classify.knn.knn as knn
from PIL import Image
import numpy as np

digits = datasets.load_digits()
datas = digits.data
targets = digits.target
target_name = digits.target_names

x_train,x_test,y_train,y_test = train_test_split(datas,targets,test_size=0.4)

model = knn.Knn()
model.fit(x_train,y_train)

err = 0
for index,item in enumerate(x_test):
    print(item)
    res = model.predict(item)
    if y_test[index] != res:
        err+=1
        print("实际是{0},识别结果是{1}".format(y_test[index],res))
print(1-err/len(x_test))

def load_img(num = 1):
    img_path = "D:/work/code/zhangyingwei/python/python-demos/input/ml/classify/knn/{0}.jpg".format(num)
    # print(img_path)
    img = Image.open(img_path)
    img = img.convert("L")
    img = img.resize((8,8))
    img_arr = np.asarray(img)
    # print(img_arr)
    img_arr = img_arr.flatten()
    return np.abs(img_arr-np.tile([255],len(img_arr)))

for i in range(10):
    img = load_img(num=i)**0.5
    # print(img)
    res = model.predict(img)
    print("image is {0},and result is {1}".format(i,res))