# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:44:49 2019

@author: AbeerJaafreh
"""


from flask import * 
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    con=sqlite3.connect("stocks.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from  stocks")
    rows=cur.fetchall()
    return render_template("view.html",rows=rows)


if __name__=="__main__":
    app.run()