# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:10:15 2020

@author: shakil
"""

import matplotlib
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import binom

matplotlib.use('webagg')

class BezierDrawer(object):
    def __init__(self, polygon, ax):
        self.polygon=polygon
        self.x_points=list(polygon.get_xdata())
        self.y_points=list(polygon.get_ydata())
        self.canvas=polygon.figure.canvas
        self.ax_main=polygon.axes
        self.ax=ax
        
        #User selecting points
        self.cid=self.canvas.mpl_connect('button_press_event', self)
        
        #Create Bézier curve
        line_bezier=Line2D([], [], c=polygon.get_markeredgecolor())
        self.bezier_curve=self.ax_main.add_line(line_bezier)

    def __call__(self, event):
        #Ignore the points selected outside axes
        if event.inaxes!=self.polygon.axes:
            return

        #Add selected points
        self.x_points.append(event.xdata)
        self.y_points.append(event.ydata)
        self.polygon.set_data(self.x_points, self.y_points)

        #Rebuild Bézier curve and update canvas
        self.bezier_curve.set_data(*self._build_bezier())
        self._update_bernstein()
        self._update_bezier()

    def _build_bezier(self):
        x, y=Bezier(list(zip(self.x_points, self.y_points))).T
        return x, y

    def _update_bezier(self):
        self.canvas.draw()

def Bernstein(n, k):
    coefficient=binom(n, k)

    def _bpoly(x):
        return coefficient*x**k*(1 - x)**(n - k)

    return _bpoly

def Bezier(points, num=200):
    N=len(points)
    t=np.linspace(0, 1, num=num)
    curve=np.zeros((num, 2))
    for ii in range(N):
        curve+=np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve

fig, ax1=plt.subplots(1, figsize=(12, 5))

line=Line2D([], [], ls='--', c='#666666',marker='o', mew=2, mec='#204a87')
ax1.add_line(line)

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_title("Bézier curve")

#Create BezierDrawer
bezier=BezierDrawer(line, ax1)

plt.show()