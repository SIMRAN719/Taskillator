from application.__init__ import app
from flask import Flask, url_for,request,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login=LoginManager()
login.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signup', methods=['GET'])
def signup():
    return render_template('Signup.html')

@app.route('/SignIn',methods=['GET','POST'])
def signin():
    form=LoginManager()
    if form.validate_on_submit():
        Flask.flash('Logged in successfully')
    return render_template('Signin.html')

@app.route('/Home')
def home():
    return render_template('Home.html')