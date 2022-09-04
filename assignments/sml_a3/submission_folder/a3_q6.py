# -*- coding: utf-8 -*-
"""a3_q6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ccq3dr5pE0xbxgBXKEGwDESlSLtqs457
"""

import numpy as np
import matplotlib.pyplot as plt
import random

e = 2.718

iter = 1
n = 0.1
b1, b01 = 0.5, 0.2
b2, b02 = 0.3, 0.4
class1 = []
class2 = []
for i in range(15):
  class1.append(random.uniform(1,20))
  class2.append(random.uniform(27,46))

f1, f2 = True, True
while(f1==True or f2==True):
  random.shuffle(class1)
  random.shuffle(class2)
  f1, f2 = False, False
  for x in class1:
    if (b2/(1+e**(-b1*x-b01))+b02<=0):
      f1 = True
      break
  for x1 in class2:
    if (b2/(1+e**(-b1*x1-b01))+b02>0):
      f2 = True
      break
  if (f1==True):
    y = 1
    b02new = b02 + n*y
    b2new = b2 +n*y*(1/(1+e**(-b1*x-b01)))
    b1new = b1 + n*y*x*(b2/(1+e**(-b1*x-b01))**2)*e**(-b1*x-b01)
    b01new = b01 + n*y*(b2/(1+e**(-b1*x-b01))**2)*e**(-b1*x-b01)
  elif (f2==True):
    y = -1
    b02new = b02 + n*y
    b2new = b2 +n*y*(1/(1+e**(-b1*x1-b01)))
    b1new = b1 + n*y*x1*(b2/(1+e**(-b1*x1-b01))**2)*e**(-b1*x1-b01)
    b01new = b01 + n*y*(b2/(1+e**(-b1*x1-b01))**2)*e**(-b1*x1-b01)
  b02 = b02new
  b2 = b2new
  b1 = b1new
  b01 = b01new
  n-=iter/1000000
  iter+=1
print(iter-1)

print(b1,b01,b2,b02)

class1_test, class2_test = [],[]
for i in range(100):
  class1_test.append(random.uniform(1,20))
  class2_test.append(random.uniform(27,46))