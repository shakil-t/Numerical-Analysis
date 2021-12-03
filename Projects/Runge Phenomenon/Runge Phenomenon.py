# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 07:46:08 2019

@author: shakil
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def f(x):
    return 1/(1+x**2)
    
def polynomial(x, co):
    y=0
    temp=[]
    for j in range(0, len(x)):
        for i in range(0, len(co)):
            y+=co[i]*x[j]**i
        temp.append(y)
    return temp

def diagram(style="dark_background"):
    mpl.style.use(style)
    fig, ax=plt.subplots(figsize=(9, 9), dpi=150)
    ax.set_title("n: {!r}".format(n), color='#800000')
    ax.plot(x_coordinates, y_coordinates, '#DC143C', label='f(x)')
    ax.plot(x_coordinates, polynomial(x_coordinates, p), '#F08080', label='pn(x)')
    ax.legend(fontsize=20)


constant=-5
coefficient=10

for n in range(1, 20):
    x_coordinates=[]
    y_coordinates=[]
    
    for i in range(0, n+1):
        xi=constant+(coefficient*i)/n
        x_coordinates.append(xi)
        y_coordinates.append(f(xi))
        
    p=np.polyfit(x_coordinates, y_coordinates, len(x_coordinates)-1)
    p=p[::-1]
    diagram()     
