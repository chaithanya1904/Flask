import time
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Home Page!!!</h1>"

@app.route("/pass")
def passed():
    return "<h1>Congrats u have passed the exam!!!</h1>"

@app.route("/fail")
def failed():
    return "<h1>Sorry u have failed the exam!!!</h1>"    

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<40:
        #redirect to failed end point
        time.sleep(2)
        return redirect(url_for("failed"))
    else:
        #redirect to failed end point
        time.sleep(2)
        return redirect(url_for("passed"))

if __name__=="__main__":
    app.run(debug=True)