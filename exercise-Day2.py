# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:36:13 2019

@author: AbeerJaafreh
"""

#Q1 Write a Python program to accept 2 numbers from the users and print the greatest
num1=int(input("Enter number one "))
num2=int(input("Enter number two "))

if num1>num2:
    print("greatest : ",num1)
else:
    print("greatest : ",num2)
    
#Q2 Write a Python program to create the multiplication table for a specific number that is 
#accepted from the user

num=int(input("Enter number "))
for x in range(1,11,1):
    print(num," × ",x," = ",num*x)


#Q3  Write a Python program to construct the following pattern, using a nested for loop.
for x in range(5):
    print(sep="/n")
    for y in range(x):
        print("*",end="")
        
for x in range(5,0,-1):
    print(sep="\n")
    for y in range(x):
        print("*",end="")
#solution
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
#Q4
letters=["x","y","z","a","b","c"]
for i in letters:
    if i=="a":
        continue
    elif i=="c":
        break
    print(i)
  
    #solution 
"""
    x
    y
    z
    b
"""

#Q5
for x in range (12,25,3):
    print (x)
    #soution
"""   
12
15
18
21
24
"""

#Q6
i=1
while i<6:
    print(i)
    if i==3:
        break
    i +=1
    #solution
"""
1
2
3
"""
#Q7
summ=0
number=int(input("Enter number "))
for i in range(0,number+1,1):
    summ+=i
print ("sum from 0 to ",number," = ",summ)

#solution
"""
Enter number 3
sum from 0 to  3  =  6
"""

#Q8
number1=int(input("Enter number "))
if number1%2==0:
    print(number1,"is Even")
else:
    print(number1,"is Odd")
    
    #solution
    """
    Enter number 6
    6 is Even
    
    Enter number 5
    5 is Even
    """


#Q9
for x in range(1,9):
    print("\n")
    s=10-x
    for i in range(s):
        print(end="  ")
    for i in range(x):
        print(i+1,sep=" ",end=" ")
        if i==(x-1):
            for z in range(i,0,-1):
                print (z,sep=" ",end=" ")
                
for x in range(9,0,-1):
    print("\n")
    s=10-x
    for i in range(s):
        print(end="  ")
    for i in range(x):
        print(i+1,sep=" ",end=" ")
        if i==(x-1):
            for z in range(i,0,-1):
                print (z,sep=" ",end=" ")
                
                #solution
                """
                  1 

                1 2 1 

              1 2 3 2 1 

            1 2 3 4 3 2 1 

          1 2 3 4 5 4 3 2 1 

        1 2 3 4 5 6 5 4 3 2 1 

      1 2 3 4 5 6 7 6 5 4 3 2 1 

    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 

  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 

    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 

      1 2 3 4 5 6 7 6 5 4 3 2 1 

        1 2 3 4 5 6 5 4 3 2 1 

          1 2 3 4 5 4 3 2 1 

            1 2 3 4 3 2 1 

              1 2 3 2 1 

                1 2 1 

                  1 
                """
        
    

#Q10
while True:
    try:
        x=int(input("Enter number "))
        print(x)
        break
    except(ValueError):
        print("No valid integer !  Please try again ...")
        
        #solution
        """
        Enter number 3.2
        No valid integer !  Please try again ...
        
        Enter number 3
        3
        """


#Q11
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("Value of b = ",b)
except(ZeroDivisionError,NameError):
    print("\n Error Occurred and Handled")
    
    #solution
    #Error Occurred and Handled