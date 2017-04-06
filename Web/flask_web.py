#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/18 22:31
# @Author  : GHL
# @File    : flask_web.py


from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return "welcome here!"


@app.route('/login')
def login():
    return 'login success'

if __name__=='__main__':
    app.run('127.0.0.1', 80, debug=True)

