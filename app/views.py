# -*- coding: utf-8 -*-
# from werkzeug import secure_filename
import os

import sqlite3
from flask import Flask
from flask import flash, redirect, render_template, request
from flask import session, url_for
from os import path
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from Models import User
from config import db
from config import app
from flask import g
from flask.ext.bootstrap import Bootstrap


DATABASE = './data.sqlite'
manager = Manager(app)
db.create_all()
bootstrap = Bootstrap(app)

name = username = nickname =email = password = state = ""
numberBook = matchBook = 0
fromUserame = toUserName = message1 = message2 = message3 = message4 = message5 = ''
username = pic = title = author = edition = description = ''

@app.route('/')
def hello_world():
    return render_template('My_profile.html')
    '''
    username = 'jiang'
    password = '2222'
    if db.session.query(User).filter_by(username='jiang').count() < 1:
       user = User(name =name, username = username, nickname = nickname,
                   numberBook = numberBook,  matchBook = matchBook, email = email,
                    password = password, state  = state)
       db.session.add(user)
       db.session.commit()

    else:
     print('user is exist')
   # for name, fullname in session.query(User.name, User.fullname):
   # print(name, fullname)
    flash(('success', 'Registration successful!'))
    #return render_template('home111.html')
    '''
@app.route('/SR', methods=['GET', 'POST'])
def searchR() :
    bookname = request.form.get('bookname')
    print 'hello'
    print bookname
    return render_template('Request_Results.html',name = 'jiangd')
   # return render_template('Search_Results.html')

@app.route('/search1', methods=['GET', 'POST'])
def query():
    bookname = request.form.get('bookname')  #
    print bookname
    if User.query.filter_by(username='jang').count() >= 1 :
        re = User.query.filter_by(username='jang').first().username
    #re = db.session.query(User).filter(User.username == bookname).password
    print re
    return ('uu')

@app.route('/search2', methods=['GET', 'POST'])
def insert():
    bookname = request.form.get('bookname')  #
    user = 'jiang'
    pw = '2222'
    if db.session.query(User).filter_by(username=bookname).count() < 1:
        user = User(username=bookname)
        db.session.add(user)
        db.session.commit()
    print bookname
    return (bookname)
@app.route('/search3', methods=['GET', 'POST'])
def delete():
    bookname = request.form.get('bookname')  #
    user = User.query.filter_by(username = bookname).first() #步骤一(username = bookname)
   # user.delete()  # 删除方法1
    db.session.delete(user)  # 删除方法2
    db.session.commit()
    print bookname
    return (bookname)

@app.route('/search', methods=['GET', 'POST'])
def change():
    bookname = request.form.get('bookname')  #\
    user = User.query.filter_by(username=bookname).first()
    user.username = 'newname'  # 更新方法1
    #user.update({'username': '[newname]'})  # 更新方法2
    db.session.commit()
    print bookname
    return (bookname)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = path.abspath(path.dirname(__file__))
        upload_path = path.join(basepath, 'static/uploads')
        # f.save(upload_path,secure_filename(f.filename))
        f.save(upload_path, (f.filename))

        return redirect(url_for('upload'))
    return render_template('upload.html')

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        os.abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
@app.route('/q')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_first_request
def before_request():
    g.db = connect_db()
    print('conn suss')

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


if __name__ == '__main__':
    app.run(debug=True)
