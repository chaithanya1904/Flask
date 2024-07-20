from flask import Flask,render_template

from employees import employees_data

app = Flask(__name__,template_folder="templates")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/employees")
def employees():
    return render_template("emp.html",title="Employees",emps=employees_data)

@app.route("/managers")
def managers():
    return render_template("managers.html",title="Managers",emps=employees_data)

@app.route("/salespersons")
def salespersons():
    return render_template("salespersons.html",title="Sales Persons",emps=employees_data)

if __name__=="__main__":
    app.run(debug=True)