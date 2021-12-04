# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 01:41:58 2019

@author: shakil
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def polynomial(x, co):
    y=0
    temp=[]
    for j in range(0, len(x)):
        for i in range(0, len(co)):
            y+=co[i]*x[j]**i
        temp.append(y)
    return temp

def diagram(style="seaborn"):
    mpl.style.use(style)
    fig, ax=plt.subplots(figsize=(10, 10))
    ax.set_title("Least Squares of Asa's data", color='#800000')
    ax.scatter(x_coordinates, y_coordinates, c="#a2b7d2")
    ax.plot(x_coordinates, polynomial(x_coordinates, p), '#F08080', label='pn(x)')
    ax.legend()

x_coordinates=np.arange(1, 13)
y_coordinates=[5.5, 2.5, 2, 2.5, 5.5, 6, 4.5, 4, 3.5, 5, 4, 3]

p=np.polyfit(x_coordinates, y_coordinates, 1)
p=p[::-1]
diagram()
