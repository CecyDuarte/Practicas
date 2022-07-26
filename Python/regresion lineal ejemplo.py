# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:10:15 2020

@author: almac
"""

import numpy as np
x = np.array([0,1,2,3,4,5])
y = np.array([0,0.8,0.9,0.1,-0.8,-1])
print(x)
print(y)

p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,3)
print(p1)
print(p2)
print(p3)

import matplotlib.pyplot as plt
plt.plot(x,y,'o')
xp = np.linspace(-2,6,100)
plt.plot(xp,np.polyval(p1,xp),'r-')
plt.plot(xp,np.polyval(p2,xp),'b--')
plt.plot(xp,np.polyval(p3,xp),'m:')
yfit = p1[0] * x + p1[1]
yresid= y - yfit
SSresid = np.sum(yresid**2)
SStotal = len(y) * np.var(y)
rsq = 1 - SSresid/SStotal
print(yfit)
print(y)
print(rsq)

from scipy.stats import linregress
slope,intercept,r_value,p_value,std_err = linregress(x,y)
print(r_value**2)
print(p_value)
plt.show()