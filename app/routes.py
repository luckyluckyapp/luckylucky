from flask import render_template, flash, redirect, request, Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests as req
import re
import datetime
from app import app, models


# if __name__ == '__main__':
#     app.run()

from app.models import Orderform

aaa = req.get("http://www.luckyluckycatering.com/lunch-menu")
soup = BeautifulSoup(aaa.text,'html.parser')
mon = re.findall("Monday:[^.]*\.", aaa.text)[0]
tue = re.findall("Tuesday:[^.]*\.", aaa.text)[0]
wed = re.findall("Wednesday:[^.]*\.", aaa.text)[0]
thur =re.findall("Thursday:[^.]*\.", aaa.text)[0]
fri =re.findall("Friday:[^.]*\.", aaa.text)[0]

day = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
wday = day.weekday()

db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index(methods=['GET', 'POST']):
	mon1 =mon[7:]
	tue1 =tue[8:]
	wed1 =wed[10:]
	thur1=thur[9:]
	fri1=fri[7:]

	dish1 = ''
	if wday == 0:
		dish1 = mon
	elif wday == 1:
		dish1 = tue
	elif wday == 2:
		dish1 = wed
	elif wday == 3:
		dish1 = thur
	elif wday == 4:
		dish1 = fri
	else:
		dish1 = 'today no lucky lucky leh!'
	
	form = Orderform()
	if request.method == 'POST':
		user=form #load the model values
		db.session.add(user) #gathers the session based data to be added in DB
		db.session.commit() #Adds data to DB
		flash('New order added!') #Display a message to end user at front end.
		return redirect('/submitted') # redirects upon success to your homepage.
	return render_template('index.html', dish=dish1, mon1=mon1, tue1=tue1, wed1=wed1, thur1=thur1, fri1=fri1, form=form)

# def add_user():
#     user = OrderForm(request.form['name']), request.form['numpacks']
#     db.session.add(user)
#     db.sessom.commit()
#     return redirect(url_for('/submitted'))

@app.route('/submitted')
def submitted():
	return render_template('submitted.html')

	# try:
	# 	if form_validate_on_submit():
	# 		user=Orderform() #load the model values
	# 		form.populate_obj(Orderform) #populates the form with respective values 
	# 		db.session.add(form) #gathers the session based data to be added in DB
	# 		db.session.commit() #Adds data to DB
	# 		flash('New order added!') #Display a message to end user at front end.
	# 		return redirect('/submitted') # redirects upon success to your homepage.
	# except Exception as e:
	# 	# logs the errors
	# 	db.session.rollback()
	# 	flash('There was a problem ordering. Please contact Jordan.')
	# 	return render_template('index.html', dish=dish1, mon1=mon1, tue1=tue1, wed1=wed1, thur1=thur1, fri1=fri1, form=form)