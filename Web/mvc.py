#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
    return render_template('form.html')


@app.route('/login', methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin123':
        return render_template('login-ok.html', username=username)
    else:
        return  "wrong user or password!"


if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
