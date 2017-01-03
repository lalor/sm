#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, IPAddress, NumberRange

class HostForm(FlaskForm):
    nickname = StringField('昵称', validators=[DataRequired(), Length(1, 24)])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    ip_address = StringField('IP', validators=[DataRequired(), IPAddress()])
    port = IntegerField('端口', validators=[DataRequired(), NumberRange(1000, 99999)])

    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('登录')
