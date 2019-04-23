from app import db
import datetime

class Orders(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)
    numpacks = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)  