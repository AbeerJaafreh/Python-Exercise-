# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:05:04 2019

@author: Abeer Jaafreh
"""

from functools import reduce

class Person(object):
    def __init__(self, a, b):
        self._Name= a
        self._Address= b
      
        
    def getName(self):
        return self._Name
    def setName(self,NewName):
        self._Name=NewName
    
    def getAddress(self):
        return self._Address
    
    def setAddress(self,NewAddress):
        self._Address=NewAddress
    
    def __del__( self):
        print ("I have been deleted")
        
p=Person("Hadeel","Amman")
print(p.getName())
print(p.getAddress())

del p
print("__________________________________________________________________")      
print("__________________________________________________________________")

class Employee(Person):
    def __init__(self,name,address,num,sal,job):
        super().__init__(name,address)
        self.EempoyeeNumber=num
        self.__Salary=sal
        self.__JobTilte=job
        self.__Loans=[]
        
    def getNum(self):
        return self.EempoyeeNumber
      
    
    def getSalary(self):
        return float(self.__Salary)
    
    def setSalary(self,salary):
        self.__Salary=salary
        
    def getJobTitle(self):
        return str(self.__JobTilte)
    
    def setJobTitle(self,jobTitle):
        self.__JobTilte=jobTitle
      
    def getLoans(self):
        return self.__Loans
    
    def getTotalLoans(self):
#        return self.__Loans.append(loan)
        total=0
        for x in range(len(self.__Loans)):
            total=total+self.__Loans[x]
        return total

    def getMaxLoan(self):
        if len(self.__Loans)!= 0:
            return(max(self.__Loans))
        else:
            return 0
        
    def getMinLoan(self):
        if len(self.__Loans)!=0:
            return(min(self.__Loans))
        
    def setLoans (self,NewLoans):
        self.__Loans=NewLoans
        
    def getInfo(self):
        return self.getName(),self.getAddress(),self.getJobTitle(),self.getSalary()

    def getDict(self,dic):
        newDic=reduce(lambda x,y :x if x>y else y ,dic,0)
        return newDic 
       

class Student(Person):
    def __init__(self,StdNumber,name,address,Subject,Marks):
        self.number=StdNumber
        super().__init__(name,address)
        self.__subject=Subject
        self.__marks=Marks
    def getSubject(self):
        return self.__subject
    def setSubject(self,string):
        self.__subject=string
    def getMarks(self):
        return self.__marks
    
    def setMarks(self,string):
        self.__marks=string
    def getAvg(self):
        x=self.__marks.values()
        x1=sum(x)
        return x1/len(x)
    
    def getAMarks(self,dic):
        newList={}
        for k,v in dic.items():
            if v>=90:
                newList.update({'name':self.getName()})
                newList.update({k:v})
                
        #print(k,v)
        print(newList)
        return ""
            
    
    def printInfo(self):
        return self.number,self.getName(),self.getAddress(),self.getSubject(),self.getMarks(),"avg =",self.getAvg()
        
#*********************************************************************************

employee1=Employee("Ahmad Yazan","Amman,Jordan",1000,500,"HR Consultan")
employee1.setLoans([434,200,1020])

employee2=Employee("Hala Rana","Aqaba,Jordan",2000,750,"Department Manager")
employee2.setLoans([150,3000,250])

employee3=Employee("Maram Ali","Mafraq,Jordan",3000,600,"HR S Consultan")
employee3.setLoans([304,1000,250,300,500,235])

employee4=Employee("Yasmeen Mohammad","Karak,Jordan",4000,865,"Director")
employee4.setLoans([])


Student1=Student(20191000,"Khalid Ali"     ,"Irbid, Jordan"  ,"History"         ,{'English':80,'Arabic':80,'Art':75,'Managment':80})
Student2=Student(20182000,"Reem Hani"      ,"Zarqa, Jordan"  ,"Software Eng"    ,{'English':80,'Arabic':90,'Managment':75,'Calculas':85,'OS':73,'Programming':90})
Student3=Student(20161001,"Nawras Abdullah","Amman, Jordan"  ,"Arts"            ,{'English':83,'Arabic':92,'Art':90,'Managment':70})
Student4=Student(20172030,"Amal Raed"      ,"Tafelah, Jordan","Computer Eng"    ,{'English':83,'Arabic':94,'Managment':70,'Calculas':80,'OS':79,'Programming':91})

#*********************************************************************************
#exersice 1
employeesList=[employee1.getInfo(),employee2.getInfo(),employee3.getInfo(),employee4.getInfo()]
print(employeesList)
print("__________________________________________________________________")      
#*********************************************************************************
#exersice 2
StudentList=[Student1,Student2,Student3,Student4]

#*********************************************************************************
#exersice 3
print(len(employeesList))
print("__________________________________________________________________")      

#*********************************************************************************
#exersice 4
print("Total Number of Students : ",len(StudentList))

#*********************************************************************************
#exersice 5
print(employee1.getName())
print(employee1.getAddress())
print(employee1.getSalary())
print(employee1.getJobTitle())
print(employee1.getTotalLoans())
print(employee1.getMaxLoan())
print(employee1.getMinLoan())
print("**********---------**********")      

print(employee2.getName())
print(employee2.getAddress())
print(employee2.getSalary())
print(employee2.getJobTitle())
print(employee2.getTotalLoans())
print(employee2.getMaxLoan())
print(employee2.getMinLoan())
print("**********---------**********")      

print(employee3.getName())
print(employee3.getAddress())
print(employee3.getSalary())
print(employee3.getJobTitle())
print(employee3.getTotalLoans())
print(employee3.getMaxLoan())
print(employee3.getMinLoan())
print("**********---------**********")      

print(employee4.getName())
print(employee4.getAddress())
print(employee4.getSalary())
print(employee4.getJobTitle())
print(employee4.getTotalLoans())
print(employee4.getMaxLoan())
print(employee4.getMinLoan())
print("__________________________________________________________________")      
#*********************************************************************************
#exersice 6+7
localAvg=[]   
for std in range(len(StudentList)):
    print("\n","Student",std+1," : \n",StudentList[std].printInfo())
    localAvg.append(StudentList[std].getAvg())
highest=reduce(lambda a,b :a if a>b else b ,localAvg)
print("\n hightest Avg : ",highest)


#*********************************************************************************
#exersice 8+9
EmployeesList=[employee1,employee2,employee3,employee4]
employeesList2=[employee1.getMaxLoan(),employee2.getMaxLoan(),employee3.getMaxLoan(),employee4.getMaxLoan()]
print(employeesList2)
print("__________________________________________________________________")      

#exersice 8
print(reduce(lambda a,b : a if a<b else b, employeesList2))
print("__________________________________________________________________")      

#exersice 9
print(reduce(lambda a,b : a if a>b else b, employeesList2))
print("__________________________________________________________________")      

#*********************************************************************************
#exersice 10
Loans=[employee1.getTotalLoans(),employee2.getTotalLoans(),employee3.getTotalLoans(),employee4.getTotalLoans()]
print("Emp 1 Loans:",employee1.getLoans(),"Loans Total :",employee1.getTotalLoans())
print("Emp 2 Loans:",employee2.getLoans(),"Loans Total :",employee2.getTotalLoans())
print("Emp 3 Loans:",employee3.getLoans(),"Loans Total :",employee3.getTotalLoans())
print("Emp 4 Loans:",employee4.getLoans(),"Loans Total :",employee4.getTotalLoans())

summation=0
for i in range(len(Loans)):
    summation=summation+Loans[i]
print("The Total Loans Across All Employee :",summation)
print("__________________________________________________________________")      

#*********************************************************************************
#exersice 11

LoanDictionary={employee1.getNum():employee1.getLoans(),employee2.getNum():employee2.getLoans(),employee3.getNum():employee3.getLoans(),employee4.getNum():employee4.getLoans()}
print("LoanDictionary : =",LoanDictionary)
print("__________________________________________________________________")      

#*********************************************************************************
#exersice 12


#*********************************************************************************
#exersice 13

#*********************************************************************************
#exersice 14
salary=[employee1.getSalary(),employee2.getSalary(),employee3.getSalary(),employee4.getSalary()]
print(max(salary))
print("__________________________________________________________________")      

#*********************************************************************************
#exersice 15
print(min(salary))

print("__________________________________________________________________")      

#exersice 16
sum2=0
for i in range(len(salary)):
    sum2=sum2+salary[i]
print(sum2)
print("__________________________________________________________________")      

#exersice 17
del employee1       
del employee2       
del employee3     
del employee4     
print("__________________________________________________________________")      















