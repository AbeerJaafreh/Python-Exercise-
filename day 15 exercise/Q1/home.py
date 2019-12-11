# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 12:58:01 2019

@author: AbeerJaafreh
"""


from flask import *
import sqlite3

from flask import * 
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html");

@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=='POST':
        data=request.form
        return render_template("view.html",data=data)
    else:
        print("Error")
        

if __name__=="__main__":
    app.run()
