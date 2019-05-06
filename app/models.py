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

    def __repr__(self):
        return '<User {}>'.format(self.name)  

class Orderform(ModelForm):
    class Meta:
        model = Orders