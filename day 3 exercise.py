# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:35:24 2019

@author: AbeerJaafreh
"""
#Q1 Write a Python program to print each item in a list in new line.

list1=[10,2,5,63,1,5,6,9,5]
for x in list1:
    print(x)
"""Solution
10
2
5
63
1
5
6
9
5
"""

#Q2  Write a Python program to sum all the items in a list and print the sum.

list1=[10,2,5,63,1,5,6,9,5]
print("sum = ",sum(list1))
"""Solution
sum =  106
"""

#Q3 3.Write a Python program to get the largest number from a list.
list1=[10,2,5,63,1,5,6,9,5]
print("largest = ",max(list1))
"""Solution
largest =  63
"""

#Q4 Write a Python program to remove duplicates from the following list
a = [10,20,30,20,10,50,60,40,80,50,40]
print(set(a))
"""Solution
{40, 10, 80, 50, 20, 60, 30}
"""

#Q5 5. Write a Python program to check a list is empty or not
a = [10,20,30,20,10,50,60,40,80,50,40]

if len(a)==0:
    print("Empty")
else:
    print("Not Empty ")
    
"""Solution
Not Empty 
"""

#Q6 Write a Python program to create a tuple with different data types and print each item in a new line
new_tuple = ( "Abeer",["Python",0,1,0,1],1.2,20)
for x in new_tuple:
    print(x)
    
"""Solution
Abeer 
['Python', 0, 1, 0, 1] 
1.2 
20
"""

#Q7 Write a Python program to iteration over sets, use the set num_set = set([0, 1, 2, 3, 4, 5])
num_set = set([0, 1, 2, 3, 4, 5])
for x in num_set:
    print (x)
"""Solution
0
1
2
3
4
5
"""
#Q8
s1={2,3,6,6,33,12,55,10}
s2={3,6,2,55,11,22,15}
print ("intersection s1 , s2 = ",s1 & s2)

"""Solution
intersection s1 , s2 =  {2, 3, 6, 55}
"""

#Q9
setx=set(["green","blue"])
sety=set(["yellow","blue"])
seta=setx|sety
print(seta)
"""Solution
{'blue', 'green', 'yellow'}
"""
#Q10
seta=set([5,10,3,15,2,20])
print(len(seta))
"""Solution
6
"""

#Q11
dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic4={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
"""Solution
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

#Q12
a="Hello,World!"
print(a[1])
print(a[2:5])
print(b[-5:-2])
print(len(a))
print(a.lower())
print(a.replace("H","J"))

"""Solution
e
llo
orl
12
hello,world!
Jello,World!
"""
