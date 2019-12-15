from flask import Flask, redirect, url_for, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ["POST"])
def login():
    msg = ""
    if request.method == "POST":
        try:
            status=""
            username = request.form["username"]
            password = request.form["password"]
            with sqlite3.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("SELECT UserName, Password FROM Login where UserName='%s' and Password = '%s'"%(username,password))
                rows = cur.fetchall()
                
                if rows:
                    msg="Done"
                    return render_template('Home.html')

                else:
                    return render_template('index.html')
        except:
            con.rollback()
            msg = "faild login"
        finally:
            con.close()




@app.route('/logout')
def logout():
    return redirect("/")
    session['']


@app.route('/department')
def department():
      return render_template('addDepartment.html')
  
    
@app.route('/addDepartment',methods=["GET","POST"])
def addDepartment():
   msg = "msg"
   if request.method == "POST":
        try:
            departmentName = request.form["deptname"]
            locationName = request.form["locID"]
            with sqlite3.connect("Org.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into departments (department_name, location_id) values (?,?)", (departmentName, locationName))

                con.commit()
                msg = "Successfully Add Department"
        except:
            con.rollback()
            msg = "we can not the Department to the list"
        finally:
            return render_template('addDepartment.html', msg=msg)
            con.close()
            
@app.route('/showdepartment')
def showdepartment():
        con = sqlite3.connect("Org.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from departments")
        rows = cur.fetchall()
        return render_template('show_dapartment.html',rows = rows)



@app.route('/showemployee')
def showemployee():
           departmentID = request.args.get('depID')
           try:
                with sqlite3.connect("Org.db") as con:
                    cur = con.cursor()
                    cur.execute("select * from employees where department_id =?",departmentID)
                    rows = cur.fetchall()
                    for row in rows:
                        print(row[0])
                    return render_template('showEmployees.html',rows = rows)
           except:
                con.rollback()
                msg = "faild login"
                print("Not Done")
           finally:
                con.close()
        
@app.route('/editemployee')
def updateemployee():
    employeeID = request.args.get('employeeID')
    try:
        with sqlite3.connect("Org.db") as con:
            cur = con.cursor()
#            cur.execute("select * from employees where employee_id =?",employeeID)
            cur.execute("select * from employees where empoyee_id =1")
            rows = cur.fetchall()
            for row in rows:
                print(row[0])
            return render_template('UpdateEmployee.html',rows = rows)
    except:
        con.rollback()
        print("Not Done")
    finally:
        con.close()

        
        

    
#    return render_template("UpdateEmployee.html" )

        
#@app.route('/deleteemployee')
#def updateemployee():
#  
#        


if __name__ == '__main__':
    app.run()