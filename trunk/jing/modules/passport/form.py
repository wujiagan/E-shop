# -*- coding: utf-8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    SUCCESS = 0
    FAILED = -1
    register_username = TextField(u'用户名', [validators.Length(min=4, max=25)])
    register_password = PasswordField(u'密码', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField(u'重复密码')
    
class LoginForm(Form):
    SUCCESS = 0
    FAILED = -1
    login_username = TextField(u'用户名', [validators.Length(min=6, max=35)])
    login_password = PasswordField(u'密码', [
        validators.Required(),
    ])

class ChangePasswordForm(Form):
    current_password = PasswordField(u'当前密码', [
        validators.Required(),
    ])
    new_password = PasswordField(u'新密码', [
        validators.Required(),
        validators.Length(min=6),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField(u'重复密码')