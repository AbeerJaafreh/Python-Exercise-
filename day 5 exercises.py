# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:54:13 2019

@author: AbeerJaafreh
"""
print('Q1------------------------------------------------')
class Employee():
        def __init__(self, EmpNumber, Name,Address,Salary,jobTitle): 
            self.empNumber=EmpNumber
            self.__name=Name
            self.__address=Address
            self.__salary=Salary
            self.__job=jobTitle
        
        def getName(self):
            return self.__name
        def getAddress(self):
            return self.__address
        def getSalary(self):
            return self.__salary
        def getJobTitle(self):
            return self.__job
            
        def setAddress(self,newAddress):
            self.__address=newAddress
        
        def __del__(self):
            print(self.getName(),'have been deleted')
        
        def getPrint(self):
            return self.empNumber
            return self.__name
            return self.__address
            return self.__salary
            return self.__job

            

            
        
emp=Employee(1,"Abeer","Amman",300,"programmer")
print("ID : ",emp.empNumber)
print("Name : ",emp.getName())
print("Address :",emp.getAddress())
emp.setAddress("Karak")
print("New Address :",emp.getAddress())
print("Salary : ",emp.getSalary())
print("Job Title : ",emp.getJobTitle())

del emp
print("\n \n")


print('Q2 create new Object------------------------------------------------')
Employee1=Employee(1,"Mohammad Khalid","Amman, Jordan",500,"Consultant")
Employee2=Employee(2,"Hala Rana","Aqaba, Jordan",750,"Manager")
print("\n \n")

print('Q3------------------------------------------------')
print("Employee 1 Information ")
print("    Employee Number : ",Employee1.empNumber)
print("    Name : ",Employee1.getName())
print("    Address : ",Employee1.getAddress())
print("    Salary : ",Employee1.getSalary())
print("    Job Title : ",Employee1.getJobTitle(),"\n")

print("Employee 2 Information ",end="")
print(" Employee Number :",Employee2.empNumber,end="")
print(" Name :",Employee2.getName(),end="")
print(" Address :",Employee2.getAddress(),end="")
print(" Salary :",Employee2.getSalary(),end="")
print(" Job Title :",Employee2.getJobTitle())
print("\n \n")

print('Q4------------------------------------------------')
Employee1.setAddress("USA")
print("\n \n")


print('Q5------------------------------------------------')
print("Employee 1 New Address :",Employee1.getAddress())
print("\n \n")


print('Q6------------------------------------------------')
del Employee1,Employee2



