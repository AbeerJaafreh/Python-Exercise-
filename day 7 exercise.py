# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:35:34 2019

@author: AbeerJaafreh
"""
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from math import *
plt.style.use('ggplot')

#Question 1-----------------------------
g= np.zeros( (1,10) , dtype=np.int32 )
g1= np.ones( (1,10) , dtype=np.int32 )
g2= np.ones( (1,10) , dtype=np.int32 ) *5

print("10 zeros : ",g)
print("10 ones : ",g1)
print("10 fives : ",g2)
print('_____________________________________________________')

#Question 2-----------------------------
a=np.arange(30,70).reshape(4,10)
print("range(30,70) : \n",a)
print('_____________________________________________________')

#Question 3-----------------------------
a=np.arange(30,70,2)
print("range(30,70) all even numbers :",a)
print('_____________________________________________________')

#Question 4-----------------------------
d=np.arange(9).reshape(3,3)
print("3x3 matrix  : \n",d)
print('_____________________________________________________')

#Question 5-----------------------------
r=np.random.random(size=(3,3))
print("random number between 0 and 1 : \n",r)
print('_____________________________________________________')

#Question 6-----------------------------
arr=np.arange(10,22).reshape(3,4)
print("3x4 matrix  :")
for x in arr:
    print(x)
print('_____________________________________________________')

#Question 7-----------------------------
arr=np.arange(0,21)
for xx in range(0,21):
    if xx>=9 and xx<16:
        arr[xx]=(-xx)
    else:
        arr[xx]=(xx)
print("change the sign of number in  range (9,15) : \n",arr)
print('_____________________________________________________')

#Question 8-----------------------------
x=[1,8,3,5]
y=np.random.randint(0,11,4)
z=x*y
print("x = ",x)
print("y = ",y)
print("x*y = ",z)
print('_____________________________________________________')

#Question 9------------------------------
matrix=np.array([
        [6,2,8,4,6,3,2],
        [11,2,33,66,55,8,3],
        [32,23,55,65,84,10,13],
        [15,23,21,45,25,26,24],
        [10,15,45,21,28,26,32]
        ])
print(matrix)
print("Number of Row & Col : ",matrix.shape)
print('_____________________________________________________')

#Question 10-----------------------------
arr3D=np.random.random((3,3,3))
print("3D array : \n",arr3D)
print('_____________________________________________________')

#Question 11-----------------------------
a=np.array([9,-1,2,5]) 
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])
print("a-b : ",a-b)
print("a*b : ",a*b)
print("a.dot(b) : ",a.dot(b))
print("a*2 : ",a*2)
print("np.sin(a) : ",np.sin(a))
print("a<3 : ",a<3)
print("a.sum() : ",a.sum())
print("a.sum(axis=0) : ",a.sum(axis=0))
print("c.sum() : ",c.sum())
print("c.sum(axis=0) : ",c.sum(axis=0))
print("a.min() : ",a.min())
print("a.max() : ",a.max())
print("a.mean() : ",a.mean())
print("a.average() : ",np.average(a))
print("a.median() : ",np.median(a))
print("a.std() : ",np.std(a))
print("a.var() : ",np.var(a))
print("c.cumsum() : ",c.cumsum())
print("a[1:2] : ",a[1:2])
print("a[2:] : ",a[2:])
print("c[-1] : ",c[-1])
print('_____________________________________________________')

#Question 12-----------------------------
X=np.arange(1,50)
y=[]
for x in X:
    y.append(x*3)
#plt.plot(X,y)
plt.plot(X,y,'b-',label='Abeer Jaafreh')
plt.legend(loc='upper left')
plt.title("Draw a line")
plt.xlabel('x-axis') 
plt.ylabel('y-axis')
plt.show()
print('_____________________________________________________')

#Question 13-----------------------------
x1=[10,20,30]
y1=[20,40,10]

x2=[10,20,30]
y2=[40,10,30]

plt.plot(x1,y1,'b-',label='line 1')
plt.plot(x2,y2,'r-',label='line 2')
plt.legend(loc='upper right')
plt.title("Two or more lines on same plot with suitable legends ")
plt.xlabel('x - axis') 
plt.ylabel('y - axis')
plt.show()
print('_____________________________________________________')

#Question 14-----------------------------
t=np.arange(0.,5.,0.2)
t2=t**2
plt.plot(t,t,'g--',t,t**2,'bs',t,t**3,'r^')
plt.show()
print('_____________________________________________________')

#Question 15-----------------------------
x=['Python','Java','PHP','JavaScript','C#','C++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(x,popularity,color=('red','black','green','blue','yellow','cyan'),align="center")

plt.title("popularity of Programming Languages ")
plt.xlabel('Languages') 
plt.ylabel('popularity')
plt.show()

print('__________________THE END ^_^ ___________________________________')


