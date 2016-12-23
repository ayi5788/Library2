# -*- coding: utf-8 -*-
from flask import *
from flask_sqlalchemy import SQLAlchemy
from os import path

SECRET_KEY = 'hard to guess string'

app = Flask(__name__)
app.config.from_object('config')

basedir = path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
'sqlite:///' + path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
db.init_app(app)



