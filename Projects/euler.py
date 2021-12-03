# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:29:23 2020

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
    y1=y+h*eval(dy)
    x+=h
    y=y1
    
print(y1)