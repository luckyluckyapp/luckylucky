import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Olam@123!?'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://vwqcpgtjuxhbys:0294ea6b4bd9bb3b5ffa0f0398a3f7b398862c217cdf040aa3a75a0d133991be@ec2-54-243-241-62.compute-1.amazonaws.com:5432/dd5oob47f4rofr'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
