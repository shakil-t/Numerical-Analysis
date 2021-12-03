# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 22:35:39 2020

@author: shakil
"""

print("Please enter the needed information respectively")
dy=input("y':")
x=float(input("x0:"))
y=float(input("y0:"))
h=float(input("h:"))
iterations=int(input("Number of iterations:"))
y1=0

for i in range(0, iterations):
    temp=y
    k1=h*eval(dy)
    x+=h/2
    y=y+0.5*k1
    k2=h*eval(dy)
    y=y+0.5*k2
    k3=h*eval(dy)
    x+=h/2
    y=y+k3
    k4=h*eval(dy)
    y1=temp+(1/6)*(k1+2*k2+2*k3+k4)
    y=y1

print(y1)