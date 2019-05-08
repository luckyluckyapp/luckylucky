from app import db
import datetime
from wtforms_alchemy import ModelForm

day = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
todaysdate = day.strftime("%Y-%m-%d")

class Orders(db.Model):
    __tablename__ = 'orders'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    numpack = db.Column(db.String(64), index=True, unique=False)
    date = db.Column(db.Date, unique=False)

    def __init__(self, uid, date, name, numpack):
        self.uid = uid
        self.name = name
        self.numpack = numpack
        self.date = date
            
    def __repr__(self):
        return '<User {}>'.format(self.name)  

    def serialize(self):
        return {
            'uid': self.uid, 
            'name': self.name,
            'numpack': self.numpack,
            'date': self.date
        }