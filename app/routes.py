from flask import render_template, flash, redirect, request, Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from app import app
from bs4 import BeautifulSoup
import requests as req
import re
import datetime
from app import models
import os


# if __name__ == '__main__':
#     app.run()

from app.forms import OrderForm

aaa = req.get("http://www.luckyluckycatering.com/lunch-menu")
soup = BeautifulSoup(aaa.text,'html.parser')
mon = re.findall("Monday:[^.]*\.", aaa.text)[0]
tue = re.findall("Tuesday:[^.]*\.", aaa.text)[0]
wed = re.findall("Wednesday:[^.]*\.", aaa.text)[0]
thur =re.findall("Thursday:[^.]*\.", aaa.text)[0]
fri =re.findall("Friday:[^.]*\.", aaa.text)[0]

day = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
wday = day.weekday()

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
	
	form = OrderForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.name.data, form.numpacks.data))
		return redirect(url_for('submitted'))
	return render_template('index.html', dish=dish1, mon1=mon1, tue1=tue1, wed1=wed1, thur1=thur1, fri1=fri1, form=form)
	
# def add_user():
#     user = OrderForm(request.form['name']), request.form['numpacks']
#     db.session.add(user)
#     db.sessom.commit()
#     return redirect(url_for('/submitted'))

@app.route('/submitted')
def submitted():
	return render_template('submitted.html')