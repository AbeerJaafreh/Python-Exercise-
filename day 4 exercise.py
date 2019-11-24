# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:03:58 2019

@author: AbeerJaafreh
"""
from functools import reduce
#Q1
o=lambda x=1,y=2,z=3 :x+y+z
print(o())
print(o(10))
print(o(10,20))
"""RESULT
6
15
33
"""



#Q2
def mul(numbers):
    mul=1
    for x in numbers:
        mul=mul*x
    
    print("product of all numbers : ",mul)

    
lis=[1,2,3,4,5,6,7,8,9,10]
mul(lis)
"""RESULT
product of all numbers : 3628800
"""


#Q3
mul = lambda x,y:x*y
print ( mul(7,5) )

"""RESULT
35
"""

#Q4

negative = list( filter(lambda x: x<0, range(-5,5)))
print(negative) 
"""RESULT
[-5, -4, -3, -2, -1]
"""

#Q5
x=lambda a,b,c:a+b+c
print(x(5,6,2))
"""RESULT
13
"""

#Q6
x=("Joey","Monica","Ross")
y=("Chandler","Pheobe")
z=("David","Rachel","Courtney")

result=list(zip(x,y,z))
print(result)
"""RESULT
[('Joey', 'Chandler', 'David'), ('Monica', 'Pheobe', 'Rachel')]
"""

#Q7

coin=("Bitcoin","Ether","Ripple","Litecoin")
code=("BTC","ETH","XRP","LTC")
d=dict(zip(coin,code))
print(d)
"""RESULT
{'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
"""

#Q8
def fun(variable):
    letters=['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False

sequence=['g','j','e','j','k','o','p','r']
filtered=list(filter(fun,sequence))
print(filtered)

"""RESULT
['e', 'o']
"""

#Q9
x=list(map(int,input("Enter a multiple values").split()))
print("List of students : ",x)
"""RESULT
Enter a multiple values 1 20 10
List of students :  [1, 20, 10]
"""
#Q10
def newfunc(a):
    return a*a
x=list(map(newfunc,(1,2,3,4)))
print(x)
"""RESULT
[1, 4, 9, 16]
"""

#Q11
def func(a,b):
    return a+b

a=list(map(func,[2,4,5],[1,2,3,2,4]))
print(a)
"""RESULT
[3, 6, 8]
"""

#Q12
c=map(lambda x:x+x ,filter(lambda x:(x>=3),(1,2,3,4)))

print(list(c))

"""RESULT
[6, 8]
"""


#Q13
c=filter(lambda x:(x>=3),map(lambda x:x+x,(1,2,3,4)))
print(list(c))
"""RESULT
[4, 6, 8]
"""

#Q14
from functools import reduce

lis=[1,2,3,4,5,6,7]
print('the min element in the list is : ',end='')
print(reduce(lambda a,b : a if a<b else b,lis))
"""RESULT
the min element in the list is : 1
"""

#Q15 

numbers=[1,2,3]
letters=['a','b','c']

print(list(zip(numbers,letters)))

"""RESULT
[(1, 'a'), (2, 'b'), (3, 'c')]
"""