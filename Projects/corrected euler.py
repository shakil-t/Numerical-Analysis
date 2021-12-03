# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:50:47 2020

@author: shakil
"""

print("Please enter the needed information respectively")
dy=input("y':")
x=float(input("x0:"))
y=float(input("y0:"))
h=float(input("h:"))
Σ=float(input("Σ:"))
iterations=int(input("Number of iterations:"))
y1=0
y2=0

for i in range(0, iterations):
    y1=y+h*eval(dy)
    do=True
    while(do):
        x+=h
        y=y1
        temp=eval(dy)
        x-=h
        y2=y1+(h/2)*(eval(dy)+temp)
        if abs(y2-y)<=Σ:
            x+=h
            y=y2
            do=False
print(y1)