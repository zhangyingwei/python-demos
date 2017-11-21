#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: zhangyw
@site: http://blog.zhangyingwei.com
@software: PyCharm 
@file: opencv_app.py 
@time: 2017/11/21 14:09 
"""
import os
from PIL import Image,ImageDraw
import cv2
import numpy as np

base_path = "/Users/zhangyw/PycharmProjects/python-demos"
xml_path = os.path.join(base_path,"input/demos/haarcascades","haarcascade_frontalface_default.xml")
image_path = os.path.join(base_path,"input/demos/images")

def trand_image(img):
    if img.ndim == 3:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    return gray

def read_iamge(name = "jbbw.jpg"):
    """
    read image
    :param name:
    :return:
    """
    path = os.path.join(image_path,name)
    img = Image.open(path)
    return np.asarray(img)

face_cascade = cv2.CascadeClassifier(xml_path)

img = read_iamge()
gray_img = trand_image(img)

"""
scale_factor：被检测对象的尺度变化。尺度越大，越容易漏掉检测的对象，但检测速度加快；尺度越小，检测越细致准确，但检测速度变慢。
min_neighbors：数值越大，检测到对象的条件越苛刻；反之检测到对象的条件越宽松；
minSize:检测对象的大小

该方法返回的是一个列表，每个列表元素是长度为四的元组，分别脸部的左上角的x,y值，脸部区域的宽度和高度。
"""
faces = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(40,40),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print(faces)


def get_points(face):
    x = face[0]
    y = face[1]
    w = face[2]
    h = face[3]
    p1 = (x,y)
    p2 = (x+w,y)
    p3 = (x,y+h)
    p4 = (x+w,y+h)
    return [p1,p2,p4,p3,p1]


def draw_image(faces,image = "jbbw.jpg"):
    img = Image.open(os.path.join(image_path,image))
    draw = ImageDraw.Draw(img)
    for face in faces:
        point = (face[0],face[1])
        draw.line(get_points(face),fill=128,width=2)
    del draw
    img.show()
draw_image(faces)