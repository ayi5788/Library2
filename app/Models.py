# -*- coding: utf-8 -*-
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import g
#映射
# pip install Flask_SQLAlchem
from config import db
class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String)
    username = db.Column(db.String,primary_key=True)
    nickname = db.Column(db.String, nullable = True)
    numberBook = db.Column(db.Integer, nullable = True)
    matchBook = db.Column(db.Integer, nullable = True)
    email = db.Column(db.String, nullable = True)
    password = db.Column(db.String, nullable = True)
    state = db.Column(db.String, nullable = True)
class MessageBoard(db.Model):
    __tablename__ = 'messageBoard'
    fromUserame = db.Column(db.String, primary_key = True)
    toUserName = db.Column(db.String, nullable = True)
    message1 = db.Column(db.String, nullable = True)
    message2 = db.Column(db.String, nullable = True)
    message3 = db.Column(db.String, nullable = True)
    message4 = db.Column(db.String, nullable = True)
    message5 = db.Column(db.String, nullable = True)

class myLibrary(db.Model):
    __tablename__ = 'myLibrary'
    username = db.Column(db.String, nullable = True)
    pic = db.Column(db.String, nullable = True)
    title = db.Column(db.String, nullable = False,primary_key = True)
    author = db.Column(db.String, nullable = True)
    edition = db.Column(db.String,  nullable = True)
    description= db.Column(db.String, nullable = True)
