# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:32:08 2017

@author: nlp
"""

import random
import matplotlib.pyplot as plt

vari = 0.2
xlnum = 100
train_times = 20

rand = Random()

x1 = [rand.normalvariate(1,vari) for _ in range(0,xlnum)]
x2 = [rand.normalvariate(2,vari) for _ in range(0,xlnum)]
x3 = [rand.normalvariate(1,vari) for _ in range(0,xlnum)]

y1 = [rand.normalvariate(1,vari) for _ in range(0,xlnum)]
y2 = [rand.normalvariate(2,vari) for _ in range(0,xlnum)]
y3 = [rand.normalvariate(2,vari) for _ in range(0,xlnum)]

x = x1+x2+x3
y = y1+y2+y3

plt.scatter(x,y,color='black')    #未分类
           
kind_x = [0.3,0.4,0.5]      #初始n个点即分n类
kind_y = [0.3,0.4,0.5]

kind_color = ["red","green","blue"]
plt.scatter(kind_x,kind_y,color=kind_color,s=200)
plt.show()

for _ in range(0,train_times):
    dic = {}
    label = []
    for idx in range(0,len(x)):
        long = 10           #设置一个初始远距离
        l = -1              #初始分类标签
        for kindex in range(0,len(kind_x)):     #kindex 初始分类点的索引和分类标签
            distants = pow(x[idx]-kind_x[kindex],2)+pow(y[idx]-kind_y[kindex],2)
            if distants < long:
                l = kindex
                long = distants
        label.append(l)
        if l in dic.keys():
            dic[l][0] += x[idx]
            dic[l][1] += y[idx]
            dic[l][2] += 1
        else:
            dic[l] = [x[idx],y[idx],1]
    for key in dic:
        kind_x[key],kind_y[key] = dic[key][0]/dic[key][2],dic[key][1]/dic[key][2]
    colors = [kind_color[num] for num in label]
    plt.scatter(x,y,color=colors)
    plt.scatter(kind_x,kind_y,color=kind_color,s=200)
    plt.show()
    