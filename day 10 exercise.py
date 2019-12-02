# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:36:51 2019

@author: AbeerJaafreh
"""
from sympy.plotting import plot 
import sympy as sym 
from sympy.plotting import plot3d

#Question 1 -------------------------------------
x,y,z,n,i = sym.symbols('x y z n i')
sym.init_printing() 

expr=x*2+x**3+21*x**4+10*x+1
print ("expr = ",expr.subs(x, 7))
print("expand = ",sym.expand((x+y)**2))
print("simplify = " ,sym.simplify(4*x**3+21*x**2+10*x+12))
print("limit = ", sym.limit(1/(x**2),x,sym.oo))
print("summation = ",sym.summation(2*i+i-1,(i,5,n))) 
print("integrate = ",sym.integrate(sym.sin(x)+sym.exp(x)*sym.cos(x)+sym.tan(x), x))
print("factor = ", sym.factor(x**3+12*x*y*z +3*y**2*z) ) 
print("solveset = ", sym.solveset(x -4, x))

m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2, 1, 0])
print("m1 * m2 = ",m1*m2)

plot(x**3+3, (x, -10, 10))

x, y = sym.symbols('x y')
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

print('------------------------------------------')
#Question 2 -------------------------------------
import xlsxwriter

workbook =xlsxwriter.Workbook('Question2.xlsx')
worksheet=workbook.add_worksheet()
worksheet.autofilter('A1:A6')

data=["This is Example","My first export example",1,2,3]

format=workbook.add_format()
format.set_font_color('red')
worksheet.write_column('A1',data)

worksheet.set_row(0,'A',format)
worksheet.set_row(4,'A',format)

workbook.close()


print('------------------------------------------')
#Question 3 -------------------------------------
from xlrd import open_workbook
wb = open_workbook('excel_python.xlsx')

for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (values,", ")