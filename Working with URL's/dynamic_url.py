from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to Home Page</h1>"

'''@app.route("/welcome/steve")
def welcome_steve():
    return "<h1> Welcome Steve</h1>"

@app.route("/welcome/tony")
def welcome_tony():
    return "<h1> Welcome Tony</h1>"'''

 #instead using above blocks of code for different persons we can dyamic urls as below

@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1> Welcome {name.title()} to our page!!!"

if __name__=="__main__":
    app.run(debug=True)