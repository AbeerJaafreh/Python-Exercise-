# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:43:46 2019

@author: AbeerJaafreh
"""

import sqlite3
from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter import messagebox


conn=sqlite3.connect('OrgDB.db')
c=conn.cursor()



c.execute('''CREATE TABLE OrgDB (EmpNumber int,EmplName text,EmpGender text, EmpNation real ,EmpDB text,EmpAddress text,EmpDepartment text,EmpSalary real)''')
def addEmp():
    def submit():
        number=int(Employee_Number.get())
        Employee_Number.set('')
        name=Employee_Name.get();
        Employee_Name.set('')
        gender=Employee_Gender.get();
        Employee_Gender.set('')
        nation=Employee_Nationality.get();
        Employee_Nationality.set('')
        DoB=Employee_DateofBirth.get();
        Employee_DateofBirth.set('')
        address=Employee_Address.get();
        Employee_Address.set('')
        depart=Employee_Depart.get();
        Employee_Depart.set('')
        salary=Employee_Salary.get();
        Employee_Salary.set('')
        
        c.execute(f"INSERT INTO OrgDB VALUES({number},'{name}','{gender}','{nation}','{DoB}','{address}','{depart}',{salary})")
        #conn.commit()

        messagebox.showinfo("Message", "inserted one recored ")
# =============================================================================
#         for row in c.execute("SELECT* FROM OrgDB ORDER BY EmpSalary"):
#             print (row)
# =============================================================================
            
    newChild=Toplevel(root)
    newChild.geometry("1000x700")
        
    label_Employee_Number = Label(newChild, text="Enter Employee Number")
    label_Employee_Number.grid(row=0, column=0)
    Employee_Number = StringVar()
    input_Employee_Number = Entry(newChild, textvariable=Employee_Number )
    input_Employee_Number.grid(row=0, column=1)
    
    label_Employee_Name = Label(newChild, text="Enter Employee Name")
    label_Employee_Name.grid(row=1, column=0)
    Employee_Name = StringVar()
    input_Employee_Name = Entry(newChild, textvariable=Employee_Name )
    input_Employee_Name.grid(row=1, column=1)
    
    label_Employee_Gender= Label(newChild, text="Enter Employee Gender")
    label_Employee_Gender.grid(row=2, column=0)
    Employee_Gender = StringVar()
    input_Employee_Gender = Entry(newChild, textvariable=Employee_Gender )
    input_Employee_Gender.grid(row=2, column=1)

    label_Employee_Nationality= Label(newChild, text="Enter Employee Nationality")
    label_Employee_Nationality.grid(row=3, column=0)
    Employee_Nationality = StringVar()
    input_Employee_Nationality = Entry(newChild, textvariable=Employee_Nationality )
    input_Employee_Nationality.grid(row=3, column=1)
    
    label_Employee_DateofBirth= Label(newChild, text="Enter Employee DateofBirth")
    label_Employee_DateofBirth.grid(row=4, column=0)
    Employee_DateofBirth = StringVar() 
    input_Employee_DateofBirth = Entry(newChild, textvariable=Employee_DateofBirth )
    input_Employee_DateofBirth.grid(row=4, column=1)
    
    
    label_Employee_Address = Label(newChild, text="Enter Employee Address")
    label_Employee_Address.grid(row=5, column=0)
    Employee_Address = StringVar()
    input_Employee_Address = Entry(newChild, textvariable=Employee_Address)
    input_Employee_Address.grid(row=5, column=1)

    label_Employee_Depart = Label(newChild, text="Enter Employee Depart")
    label_Employee_Depart.grid(row=6, column=0)
    Employee_Depart= StringVar()
    input_Employee_Depart = Entry(newChild, textvariable=Employee_Depart)
    input_Employee_Depart.grid(row=6, column=1)
    
    
    input_Employee_Salary = Label(newChild, text="Enter Employee Salary")
    input_Employee_Salary.grid(row=7, column=0)
    Employee_Salary = StringVar()
    input_Employee_Salary = Entry(newChild, textvariable=Employee_Salary)
    input_Employee_Salary.grid(row=7, column=1)
    
    btn = Button(newChild, text="Save" ,command=submit)
    btn.grid(row=8, column=0)

def viewEmp():
    view=Toplevel(root)
    view.geometry("1000x700")
	
    info=ScrolledText(view,width=120,height=60)	
    msg = "DataBase Information :\n"
    for row in c.execute('SELECT * FROM OrgDB'):
        
        msg = msg + f'''
        Number:       {row[0]}
        Name:         {row[1]}
        Gender:       {row[2]}
        Nationality:  {row[3]}
        Date of Birth:{row[4]}
        Adress:       {row[5]}
        Department:   {row[6]}
        Salary:       {row[7]}\n\n\n'''
 	
    info.insert(END, msg + '\n')
    info.grid(column=0,row=0)
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.geometry("1000x700")
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Add Employee",command=addEmp)
filemenu.add_command(label="View Employee",command=viewEmp)
conn.commit()

mainloop()