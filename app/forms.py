from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import datetime

day = datetime.datetime.utcnow() + datetime.timedelta(hours=+8)
todaysdate = day.strftime("%Y-%m-%d")


class OrderForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    numpacks = SelectField(u'Number of packets: ', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], validators=[DataRequired()])
    date1 = todaysdate
    submit = SubmitField('Submit Order')