# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:20:59 2019

@author: Abeer
"""

#exercise 1 
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "This is Index Page!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members Page"


    
#exercise 2 

@app.route('/ex2/<int:score>')
def scoree(score):
   return render_template('index.html',marks=score)




#exercise 3
@app.route('/ex3')
def score():
   return render_template('ex3.html') 
    

if __name__ == '__main__':
   app.run()