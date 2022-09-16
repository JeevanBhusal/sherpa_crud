import os
from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user




app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/faheem/Desktop/project/flask_login/database.db'



PORT = int(os.environ.get('PORT', 2000))






@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        employee_contact_no = request.form['employee_contact_no']
        employee_address = request.form['employee_address']
        employee_mail_address = request.form['employee_mail_address']
        Employee =Employee (first_name=first_name, middle_name=middle_name,last_name=last_name,employee_contact_no=employee_contact_no,employee_address=employee_address,employee_mail_address=employee_mail_address)
        db.session.add(Employee)
        db.session.commit()
        
    allEmployee = Employee.query.all() 
    return render_template('index.html', allEmployee=allEmployee)


@app.route('/index')
def index():
	return render_template('index.html', form = "form")    



@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', name= current_user.username)




if __name__ == '__main__':
    app.run(debug=True, port = PORT)