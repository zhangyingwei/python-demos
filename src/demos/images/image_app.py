#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: image_app.py 
@time: 2017/11/21 11:42 
"""

import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

base_path = "D:/work/code/zhangyingwei/python/python-demos"

# 显示图片的直方图
def show_image_zft():
    """
    在python中可以依靠Image对象的histogram()方法获取其直方图数据，
    但这个方法返回的结果是一个列表，如果想得到下图可视化数据
    """
    img0 = Image.open(os.path.join(base_path,"input/demos/images/0.jpg"))
    img1 = Image.open(os.path.join(base_path,"input/demos/images/1.jpg"))

    histogram0 = img0.histogram()
    histogram1 = img1.histogram()

    y = range(0,len(histogram0))

    plt.plot(y,histogram0)
    plt.plot(y,histogram1)

    plt.show()


def show_image_arr():
    img0 = Image.open(os.path.join(base_path, "input/demos/images/0.jpg"))
    img1 = Image.open(os.path.join(base_path, "input/demos/images/1.jpg"))
    h_img = img0.convert("L")
    # 显示灰度图片
    # h_img.show()
    h_arr = np.array(h_img)
    img0_arr = np.array(img0)
    print(h_arr)
    print("-------------------")
    print(img0_arr)

show_image_arr()