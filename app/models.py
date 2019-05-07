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
    date = todaysdate

    def __init__(self, uid, name, numpack):
        self.uid = uid
        self.name = name
        self.numpack = numpack
    
    def __repr__(self):
        return '<User {}>'.format(self.name)  

    def serialize(self):
        return {
            'uid': self.uid, 
            'name': self.name,
            'numpack': self.numpack
        }