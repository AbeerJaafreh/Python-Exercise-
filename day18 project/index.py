# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:00:21 2019

@author: AbeerJaafreh
"""



from flask import * 
import sqlite3
app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/success",methods=["POST"])
def success():
    msg = ""
    if request.method == "POST":
        try:
            status=""
            email = request.form["email"]
            password = request.form["password"]
            with sqlite3.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("SELECT user_Name, password FROM login where user_Name='%s' and password = '%s'"%(email,password))
                rows = cur.fetchall()
                
                if rows:
                    msg="Done"
                    return render_template('home.html')

                else:
                    return render_template('login.html')
        except:
            con.rollback()
            msg = "faild login"
        finally:
            con.close()
            
if __name__=="__main__":
    app.run()