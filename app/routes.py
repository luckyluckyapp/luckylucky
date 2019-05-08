from flask import render_template, flash, redirect, request, Flask, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests as req
import re
import datetime
from app import app, models
import time


aaa = req.get("http://www.luckyluckycatering.com/lunch-menu")
soup = BeautifulSoup(aaa.text,'html.parser')
mon = re.findall("Monday:[^.]*\.", aaa.text)[0]
tue = re.findall("Tuesday:[^.]*\.", aaa.text)[0]
wed = re.findall("Wednesday:[^.]*\.", aaa.text)[0]
thur =re.findall("Thursday:[^.]*\.", aaa.text)[0]
fri =re.findall("Friday:[^.]*\.", aaa.text)[0]

day = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
wday = day.weekday()
todaysdate = day.strftime("%Y-%m-%d")

db = SQLAlchemy(app)

from app.models import Orders

# global dish
mon1 =mon[7:]
tue1 =tue[8:]
wed1 =wed[10:]
thur1=thur[9:]
fri1=fri[7:]

dish2 = ''
if wday == 0:
	dish2 = mon
elif wday == 1:
	dish2 = tue
elif wday == 2:
	dish2 = wed
elif wday == 3:
	dish2 = thur
elif wday == 4:
	dish2 = fri
else:
	dish2 = 'today no lucky lucky leh!'

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index(methods=['GET']):
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
	
	return render_template('index.html', dish=dish1, mon1=mon1, tue1=tue1, wed1=wed1, thur1=thur1, fri1=fri1)

@app.route("/form", methods=['GET', 'POST'])

def add_order_form():
	ts = int(time.time())
	if request.method == 'POST':
		uid = ts
		name=request.form.get('name')
		numpack=request.form.get('numpack')
		date=todaysdate
		try:
			order1=Orders(
			uid=uid,
			name=name,
			numpack=numpack,
			date=date
			)
			db.session.add(order1)
			db.session.commit()
			return render_template('submitted.html', name=name)
		except Exception as e:
			return(str(e))
	return render_template('form.html', dish=dish2)

@app.route('/submitted')
def submitted():
	try:
		name=request.form.get('name')
	except:
		name=''
	return render_template('submitted.html', name=name)

@app.route("/getall")
def get_all():
    try:
        orders=Orders.query.all()
        return  jsonify([e.serialize() for e in orders])
    except Exception as e:
	    return(str(e))

### Develop logic for rendering json, and presenting in nice table