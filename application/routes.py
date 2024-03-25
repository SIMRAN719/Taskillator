from application.__init__ import app,db
from flask import Flask, url_for,request,render_template,redirect, session
from flask_sqlalchemy import SQLAlchemy
from application.authentication import valid_username,valid_password,valid_email,valid_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name=request.form['name']
        pwd=request.form['password']
        mail=request.form['email']
        if (valid_name(name) and valid_password(pwd) and valid_email(mail)):
            return redirect(url_for('home'))
        else:
            return render_template('Signup.html')
    return render_template('Signup.html')

@app.route('/SignIn',methods=['GET','POST'])
def signin():
    if request.method =='POST':
        email=request.form['email']
        pwd=request.form['passowrd']
        if (valid_email(email) and valid_password(pwd)):
            if ((email in db.email) and (pwd in db.password)):
                return redirect(url_for('home'))
            else:
                return render_template('Signin.html')
        else:
            pass
            #Flask.flash('Invalid email or password')
    return render_template('Signin.html')

@app.route('/Home')
def home():
    return render_template('TaskHome.html')