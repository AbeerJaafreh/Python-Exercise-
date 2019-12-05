from tkinter import *
from tkinter import scrolledtext, messagebox


def About():
    messagebox.showinfo('About','OOP SECOND POJECT')

def Report():
    btn = Button(text="Employees List", command=View_Employee)
    btn.grid(row=0, column=1)

    btn = Button(text="Students List", command=View_Student)
    btn.grid(row=1, column=1)



Employee_Name = []
Employee_Address = []
Employee_Salary=[]
Employee_Jop=[]

def Employees():
    def Add_To_Employee():

        Employee_Name.append(input_Employee_Name.get())
        Employee_Address.append(input_Employee_Address.get())
        Employee_Salary.append(input_Employee_Salary.get())
        Employee_Jop.append(input_Employee_Jop.get())

        print(Employee_Name)
        print()
        print(Employee_Address)

    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    label_Employee_Name = Label(newChild, text="Enter Name")
    label_Employee_Name.grid(row=0, column=0)

    input_Employee_Name = StringVar()
    input_Employee_Name = Entry(newChild, textvariable=input_Employee_Name )
    input_Employee_Name.grid(row=0, column=1)


    label_Employee_Address = Label(newChild, text="Address")
    label_Employee_Address.grid(row=1, column=0)

    input_Employee_Address = StringVar()
    input_Employee_Address = Entry(newChild, textvariable=input_Employee_Address)
    input_Employee_Address.grid(row=1, column=1)

    input_Employee_Salary = Label(newChild, text="Salary")
    input_Employee_Salary.grid(row=2, column=0)

    input_Employee_Salary = StringVar()
    input_Employee_Salary = Entry(newChild, textvariable=input_Employee_Salary)
    input_Employee_Salary.grid(row=2, column=1)

    input_Employee_Jop = Label(newChild, text="Jop Title")
    input_Employee_Jop.grid(row=3, column=0)

    input_Employee_Jop = StringVar()
    input_Employee_Jop = Entry(newChild, textvariable=input_Employee_Jop)
    input_Employee_Jop.grid(row=3, column=1)



    btn = Button(newChild, text="Save" , command=Add_To_Employee)
    btn.grid(row=4, column=0)



def View_Employee():
    print("View")

    newChild = Toplevel(root)
    newChild.geometry("1000x700")


    st = scrolledtext.ScrolledText(newChild)
    st.pack()
    fmt = '{:<8}{:<20}{}'
    for i, (Name, Address , Salary , Jop) in enumerate(zip(Employee_Name, Employee_Address , Employee_Salary , Employee_Jop)):

        st.insert(INSERT, 'Number : '+str(i)+"  Name : "+ Name + '  Address : '+Address + ' Salary : '+Salary+ ' Jop : '+ Jop +"\n" )

def Delete_Employee():
    def del_Employee():
        for i in range(len(Employee_Address)):
            print('input_Employee_Number.get()', type(int(input_Employee_Number.get())))

            if int(input_Employee_Number.get()) == i:
                Employee_Address.pop(i)
                Employee_Name.pop(i)
                Employee_Salary.pop(i)
                Employee_Jop.pop(i)
            else:
                print("Address not exist")


    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    label_Employee_Number = Label(newChild, text="Employee_Number")
    label_Employee_Number.grid(row=2, column=0)

    input_Employee_Number = StringVar()
    input_Employee_Number = Entry(newChild, textvariable=input_Employee_Number)
    input_Employee_Number.grid(row=2, column=1)

    btn = Button(newChild, text="Delete" , command=del_Employee)
    btn.grid(row=4, column=0)




Student_Name = []
Student_Address = []
Student_Subject=[]
Student_Marks=[]

# ---------------------------------------------------------------------------------------------------------------------
def Students():
    def Add_To_Student():
        Student_Name.append(input_Student_Name.get())
        Student_Address.append(input_Student_Address.get())
        Student_Subject.append(input_Student_Subject.get())
        Student_Marks.append(input_Student_Marks.get())

        print(Student_Name)
        print()
        print(Student_Address)
    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    label_Student_Name = Label(newChild, text="Enter Name")
    label_Student_Name.grid(row=0, column=0)

    input_Student_Name = StringVar()
    input_Student_Name = Entry(newChild, textvariable=input_Student_Name)
    input_Student_Name.grid(row=0, column=1)

    label_Student_Address = Label(newChild, text="Address")
    label_Student_Address.grid(row=1, column=0)

    input_Student_Address = StringVar()
    input_Student_Address = Entry(newChild, textvariable=input_Student_Address)
    input_Student_Address.grid(row=1, column=1)

    input_Student_Subject = Label(newChild, text="Subject")
    input_Student_Subject.grid(row=2, column=0)

    input_Student_Subject = StringVar()
    input_Student_Subject = Entry(newChild, textvariable=input_Student_Subject)
    input_Student_Subject.grid(row=2, column=1)

    input_Student_Marks = Label(newChild, text="Marks")
    input_Student_Marks.grid(row=3, column=0)

    input_Student_Marks = StringVar()
    input_Student_Marks = Entry(newChild, textvariable=input_Student_Marks)
    input_Student_Marks.grid(row=3, column=1)

    btn = Button(newChild, text="Save", command=Add_To_Student)
    btn.grid(row=4, column=0)


def View_Student():
    print("View")

    newChild = Toplevel(root)
    newChild.geometry("1000x700")

    st = scrolledtext.ScrolledText(newChild)
    st.pack()
    fmt = '{:<8}{:<20}{}'
    for i, (Name, Address, Subject, Marks) in enumerate(
            zip(Student_Name, Student_Address, Student_Subject, Student_Marks)):
        st.insert(INSERT, 'Number : ' + str(i) + "  Name : " + Name + '  Address : ' + Address + ' Subject : ' + Subject + ' Marks : ' + Marks + "\n")

def Delete_Student():

    def del_Student():
        for i in range(len(Student_Address)):
            print('input_Student_Number.get()', type(int(input_Student_Number.get())))

            if int(input_Student_Number.get()) == i:
                Student_Address.pop(i)
                Student_Name.pop(i)
                Student_Subject.pop(i)
                Student_Marks.pop(i)
            else:
                print("Address not exist")

    newChild = Toplevel(root)
    newChild.geometry("1000x700")
    label_Student_Number = Label(newChild, text="Student_Number")
    label_Student_Number.grid(row=2, column=0)

    input_Student_Number = StringVar()
    input_Student_Number = Entry(newChild, textvariable=input_Student_Number)
    input_Student_Number.grid(row=2, column=1)

    btn = Button(newChild, text="Delete", command=del_Student)
    btn.grid(row=4, column=0)


#----------------------------------------------------------------------------------------------------------------------


root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.geometry("1000x700")
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Report", command=Report)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#____________________________________________________________Employee_MENU

Employees_menu = Menu(menu)
menu.add_cascade(label="Employees", menu=Employees_menu)
Employees_menu.add_command(label="Add", command=Employees)
Employees_menu.add_command(label="View", command=View_Employee)
Employees_menu.add_command(label="Delete", command=Delete_Employee)



#______________________________________________________________________________Students_MENU
Students_menu = Menu(menu)
menu.add_cascade(label="Students" , menu=Students_menu)
Students_menu.add_command(label="Add", command=Students)
Students_menu.add_command(label="View", command=View_Student)
Students_menu.add_command(label="Delete" , command=Delete_Student)


About_menu = Menu(menu)
menu.add_cascade(label="About" , menu= About_menu)
About_menu.add_command(label="About" , command=About)

mainloop()