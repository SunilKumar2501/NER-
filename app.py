from werkzeug.utils import redirect
import nerapi
from db import Database
from flask import Flask,render_template,request,session
app = Flask(__name__)
dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration',methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get("user_email")
    password = request.form.get("user_pass")
    response = dbo.insert(name,email,password)
    if response:
        return render_template("login.html",message="Registration Successful, Login to proceed")
    else:
        return render_template('register.html',message = "Email already Exists")


@app.route('/perform_login',methods = ["post"])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = dbo.valid(email,password)
    if response == 1:
        return redirect("/profile")
    else:
        return render_template('login.html',messages = "Incorrect email/password")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/ner")
def ner():
    return render_template("ner.html")


@app.route("/perform_ner",methods = ["Post"])
def perform_ner():
    text = request.form.get("ner_text")
    response = nerapi.ner(text)
    # print(response)
    return render_template("ner.html",result = response)

@app.route("/logout")
def logout():
    return redirect("/")

app.run(debug = True)

