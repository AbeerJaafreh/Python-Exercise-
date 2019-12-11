from flask import * 
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html");

@app.route("/add")
def add():
    return render_template("addEmp.html")

@app.route("/savedetailes",methods=["POST","GET"])
def savedetailes():
    message=""
    if request.method=='POST':
        try:
            name=request.form["name"]
            email=request.form["email"]
            address=request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO Employees (name,email,address) values (?,?,?)",(name,email,address))
                con.commit()
                message="Employees successfully Added"
        except:
            con.rollback()
            message="we can't add the employees to the list"
        finally:
            return render_template("success.html",message=message)
            con.close()
            
@app.route("/view")
def view():
    con=sqlite3.connect("employee.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from  Employees")
    rows=cur.fetchall()
    return render_template("view.html",rows=rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleteRecords",methods=["post"])
def deleteRecords():
    id=request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur=con.cursor()
            cur.execute("DELETE from Employees where id=?",id)
            message="Records successfully deleted"
        except:
            message="can't be deleted"
        finally:
            return render_template("deleteRecords.html",message=message)
if __name__=="__main__":
    app.run()