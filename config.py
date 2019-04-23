import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Olam@123!?'
    SQLALCHEMY_DATABASE_URI = 'postgres://wwwbvuhuxuiecn:8cc3022620347c0f29ad84b0f43ab15f03db935008f65e1fdb4ac0eb4683e545@ec2-23-21-136-232.compute-1.amazonaws.com:5432/d3ionhq9q82n85'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
