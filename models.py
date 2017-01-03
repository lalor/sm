#!/usr/bin/python
#-*- coding: UTF-8 -*-
from ext import db
from flask_login import UserMixin


class Host(db.Model):
    __tablename__ = 'host'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    ip_address = db.Column(db.String(30), nullable=False)
    port = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        self.__dict__.update({k:v for k, v in kwargs.iteritems() if k != 'self'})


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __init__(self, **kwargs):
        self.__dict__.update({k:v for k, v in kwargs.iteritems() if k != 'self'})