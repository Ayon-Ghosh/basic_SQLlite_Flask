from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '97ef228e7817af51de40afb50c78e36d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(120),unique = True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable = False)
	posts = db.relationship('Post', backref = 'author', lazy = True)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.password}')"

class Post(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable = False)
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	
	def __repr__(self):
		return f"Post('{self.title}','{self.date_posted}')"

			
	

posts = [

{'author':'Ayon Ghosh',
'title':'Blog Post 1',
'content':'First Post Content',
'date_posted': 'Jan 19th 2020'},

{'author':'Koyel Ghosh',
'title':'Blog Post 2',
'content':'Second Post Content',
'date_posted': 'Jan 20th 2020'}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts = posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/register", methods = ['POST', 'GET'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))

	return render_template("register.html", title="Register", form = form)

@app.route("/login", methods = ['POST', 'GET'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
		     flash('Login Unsuccessful - please check username and password', 'danger')	
	return render_template("login.html", title="Login", form = form)


if __name__ == "__main__":
	db.create_all()
	app.run(debug = True)	