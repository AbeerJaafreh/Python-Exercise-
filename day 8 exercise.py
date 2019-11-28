# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:27:43 2019

@author: AbeerJaafreh
"""

import numpy as np
import pandas as pd

#Question 1 -------------------------------------------------------
data =[2,4,6,8,10]
s=pd.Series(data)
print(s)
"""solution 
0     2
1     4
2     6
3     8
4    10
dtype: int64
"""
#Question 2 -------------------------------------------------------
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
s1=pd.Series(d1)
print(s1)
"""solution 
a    100
b    200
c    300
d    400
e    800
dtype: int64
"""
#Question 3 -------------------------------------------------------
data = [20, 10, 150, 110, 100, 50]
s = pd.Series(data)
print( s.describe())
s.plot(kind="bar",color=['red','black','green','blue','yellow','cyan'])
"""solution 
count      6.000000
mean      73.333333
std       55.377492
min       10.000000
25%       27.500000
50%       75.000000
75%      107.500000
max      150.000000
dtype: float64
"""
#Question 4 -------------------------------------------------------
Data = {'d1':[100,200,5,400,700,100,200,50,400,700], 
        'd2':[140,0,300,400,200,140,0,700,400,200]  } 
df=pd.DataFrame(Data)
print("df describe :  \n", df.describe())
df.plot()
"""solution 
df describe :  
               d1          d2
count   10.00000   10.000000
mean   285.50000  248.000000
std    255.47831  211.911931
min      5.00000    0.000000
25%    100.00000  140.000000
50%    200.00000  200.000000
75%    400.00000  375.000000
max    700.00000  700.000000
"""
#Question 5 -------------------------------------------------------
Data= { 'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]} 
df=pd.DataFrame(Data)
print(df)
"""solution 
    X   Y   Z
0  78  84  86
1  85  94  97
2  96  89  96
3  80  83  72
4  86  86  83
"""
#Question 6 -------------------------------------------------------
dic={'names':['Bob','Jessica','Mary','John','Mel'], 
     'births': [968, 155, 77, 578, 973]}
s=pd.DataFrame(dic)
print(s)
s.plot.pie(y='births', figsize=(5, 5)) 
"""solution 
      names  births
0      Bob     968
1  Jessica     155
2     Mary      77
3     John     578
4      Mel     973
"""
#Question 7-------------------------------------------------------
import pandas as pd
data=[100,2200,300,400,500,600,700,800,900]
df=pd.DataFrame(data,columns=['Numbers'])

df.to_csv('myData.csv',sep='\t')
df=pd.read_csv('myData.csv',sep='\t',index_col=0)
print(df)
print(df.describe())
df.to_csv('myData2.csv',sep=',')
"""solution 
   Numbers
0      100
1     2200
2      300
3      400
4      500
5      600
6      700
7      800
8      900
           Numbers
count     9.000000
mean    722.222222
std     607.819418
min     100.000000
25%     400.000000
50%     600.000000
75%     800.000000
max    2200.000000
"""
#Question 8-------------------------------------------------------
dates=pd.date_range('20000101',periods=4)
df=pd.DataFrame(np.random.randn(4,2),index=dates,columns=list('AB'))
print(df)
print(df.head(2))
print(df[["A"]])
print(df[0:1])
print(df["20000102":"20000104"])
print(df.loc['20000102':'20000104', ['A']])
print(df.iloc[:, 1:2])
print(df[df> 0])
print(df[df.B> 0])
df['A'] = [100,200,300,100]
print (df)
print(df[df['A'].isin([200, 300])])
"""solution 
                   A         B
2000-01-01 -1.537992 -0.096826
2000-01-02  0.043200 -0.807631
2000-01-03 -0.489128 -0.290390
2000-01-04  0.981355 -0.922472
                   A         B
2000-01-01 -1.537992 -0.096826
2000-01-02  0.043200 -0.807631
                   A
2000-01-01 -1.537992
2000-01-02  0.043200
2000-01-03 -0.489128
2000-01-04  0.981355
                   A         B
2000-01-01 -1.537992 -0.096826
                   A         B
2000-01-02  0.043200 -0.807631
2000-01-03 -0.489128 -0.290390
2000-01-04  0.981355 -0.922472
                   A
2000-01-02  0.043200
2000-01-03 -0.489128
2000-01-04  0.981355
                   B
2000-01-01 -0.096826
2000-01-02 -0.807631
2000-01-03 -0.290390
2000-01-04 -0.922472
                   A   B
2000-01-01       NaN NaN
2000-01-02  0.043200 NaN
2000-01-03       NaN NaN
2000-01-04  0.981355 NaN
Empty DataFrame
Columns: [A, B]
Index: []
              A         B
2000-01-01  100 -0.096826
2000-01-02  200 -0.807631
2000-01-03  300 -0.290390
2000-01-04  100 -0.922472
              A         B
2000-01-02  200 -0.807631
2000-01-03  300 -0.290390
"""