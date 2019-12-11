# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:11:52 2019

@author: AbeerJaafreh
"""
import sqlite3 
con=sqlite3.connect("employee.db")
print("Database opened successfully")
con.execute("CREATE TABLE Employees (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL ,email TEXT UNIQUE NOT NULL,address TEXT NOT NULL)")

con.close()

