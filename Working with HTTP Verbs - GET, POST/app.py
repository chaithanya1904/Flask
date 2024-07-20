from flask import Flask,render_template,request,url_for,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',title="HOME")

@app.route("/checkresults",methods=['GET','POST'])
def check_results():
    return render_template("form.html",title="Results")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=str(request.form['name'])
        m1=int(request.form['sub1'])
        m2=int(request.form['sub2'])
        total_marks = m1+m2
        if total_marks >=35 :
            return render_template("result.html",name=name,s1=m1,s2=m2,total=total_marks,res="PASS",title="Results")
        else:
            return render_template("result.html",name=name,s1=m1,s2=m2,total=total_marks,res="FAIL",title="Results")
    return render_template("form.html",title="Check Results")

if __name__=="__main__":
    app.run(debug=True)