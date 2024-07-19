from flask import Flask

app=Flask(__name__)

#this is home
@app.route("/")
def home():
    return "<h1> Welcome to Flask Course!!!<h1>"

#path parameters
@app.route("/name")
def name():
    return "<h1>Hello Brother!!!<h1>"

@app.route("/addition/<val1>")
def addition(val1):
    return f"<h1> Number is {val1}<h1>"

if __name__=="__main__":
    app.run(debug=True)