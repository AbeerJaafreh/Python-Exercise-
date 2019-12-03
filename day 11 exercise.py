# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:06:36 2019

@author: AbeerJaafreh
"""

import tkinter as tk

#Question 1 ----------------------------------------------------------

root=tk.Tk()
def Submit():
    if txt1.get()=="Orange" and txt2.get()=="CodingAcademy":
        tk.messagebox.showinfo("login","Successful login")
    else:
        tk.messagebox.showerror("Error login")
    
name=tk.Label(root,text="Name").grid(row=0,column=0)
txt1=tk.StringVar()
box1=tk.Entry(root,textvariable=txt1).grid(row=0,column=1)

txt2=tk.StringVar()
password=tk.Label(root,text="Password").grid(row=1,column=0)
box2=tk.Entry(root,textvariable=txt2).grid(row=1,column=1)

submit=tk.Button(root,text="Submit",command=Submit).grid(row=4,column=0)
root.geometry("200x200+100+200")
root.mainloop()

#Question 2 ----------------------------------------------------------
from tkinter import *
from tkinter import scrolledtext
root=Tk()
  
def Pressed():
    dialog_title="Message Box"
    dialog_text="This is a message"
    tk.messagebox.showinfo(dialog_title,dialog_text)
    
def child1():
    def esc():
        c.destroy()
        
    c=Toplevel(root)
    num=Label(c,text="Emp Number").grid(row=0,column=0)
    box1=Entry(c).grid(row=0,column=1)
    
    name=Label(c,text="Emp Name").grid(row=1,column=0)
    box2=Entry(c).grid(row=1,column=1)
    
    submit1=Button(c,text="exit",command=esc).grid(row=4,column=0)

def child2():
    window=Toplevel(root)
    window.title("child wondow 2")
    window.geometry('350x200+230+130')
    scrollbar=Scrollbar(window)
    
    txt=scrolledtext.ScrolledText(window,width=50,height=70)
    mylist=Listbox(window,yscrollcommand=scrollbar.set)
    for i in range(20):
        mylist.insert(END,"The count is ",str(i))
    mylist.pack(side=LEFT,fill=BOTH)
    txt.grid(column=0,row=0)
    
    
btn1=Button(root,text="Open message",command=Pressed).grid(row=0,column=0)
btn2=Button(root,text="Open child wondow 1",command=child1).grid(row=1,column=0)
btn3=Button(root,text="Open child wondow 2",command=child2).grid(row=2,column=0)

root.mainloop()

#Question 3 ----------------------------------------------------------
from tkinter.colorchooser import askcolor

window=Tk()
window.geometry('350x200')

def getColor():
    color=askcolor()
    name = color[1]
    print(name)
    window.configure(background=name)

Button(text='Select Color',command=getColor).pack()
mainloop()