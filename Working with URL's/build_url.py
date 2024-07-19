import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Home Page!!!</h1>"

@app.route("/pass/<sname>/<int:marks>")
def passed(sname,marks):
    return f"<h1>Congrats {sname} u have passed the exam with {marks} marks!!!</h1>"

@app.route("/fail/<sname>/<int:marks>")
def failed(sname,marks):
    return f"<h1>Sorry {sname} u have failed the exam with {marks} marks!!!</h1>"    

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<40:
        #redirect to failed end point along with the input values
        time.sleep(2)
        return redirect(url_for("failed",sname=name,marks=num))
    else:
        #redirect to passed end point along with the input values
        time.sleep(2)
        return redirect(url_for("passed",sname=name,marks=num))

if __name__=="__main__":
    app.run(debug=True)