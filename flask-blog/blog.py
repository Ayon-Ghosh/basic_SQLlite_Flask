#blog.py ----controller
#imports
from flask import Flask,render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps
#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
	@wraps(test)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
		    flash('you need to log in first')
		    return redirect(url_for('login'))
	return wrap	    	


@app.route('/', methods = ['GET','POST'])
def login():
  error = None
  status_code = 200
  if request.method =='POST':
	  if(request.form['username']!=app.config['USERNAME']) or (request.form['password']!=app.config['PASSWORD']):
		    error = 'invalid credential - please try again'
		    status_code = 401	
		    return render_template('login.html', error = error),status_code	
	  else:
	        session['logged_in'] = True
	        return redirect(url_for('main'))
  return render_template('login.html', error = error),status_code
	
@app.route('/main')	
@login_required
def main():
	g.db = connect_db()
	cur = g.db.execute("SELECT * from posts")
	posts = [dict(title = row[0],post = row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html',posts = posts)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('you were logged out')	
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug = True) 