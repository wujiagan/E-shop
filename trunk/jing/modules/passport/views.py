# -*- coding: utf-8 -*-
from flask import request, flash, url_for, redirect, current_app
from flask.views import MethodView
from flask.ext.login import login_user, logout_user, current_user
from werkzeug import check_password_hash, generate_password_hash

from jing.core.templates import render_template
from jing.core.database import dbs

from ..passport.models import Role, User
from .form import RegistrationForm, LoginForm, ChangePasswordForm
import json
import logging
logger = logging.getLogger()

class IsRegistered(MethodView):
    def post(self):
        args = request.form.to_dict()
        logger.debug(args)
        if User.query.filter_by(username = args['param']).first():
            return u'该账号已经注册'
        return 'y'

class Register(MethodView):
    def post(self):
        logger.debug(request.form)
        form = RegistrationForm(request.form)
        ret = {'code' : form.FAILED}
        try:
            user = User()
            user.username = form.register_username.data
            user.password = generate_password_hash(form.register_password.data)
            
            role = Role.query.filter_by(name = 'member').first()
            if not role:
                role = Role()
                role.name = 'member'
                role.description = 'description'
                dbs.session.add(role)
            user.roles = [role]
            dbs.session.add(user)
            dbs.session.commit()
            login_user(user)
            ret['code'] = form.SUCCESS
        except Exception, e:
            logger.debug(e)
        return json.dumps(ret)


class Logout(MethodView):
    def get(self):
        logout_user()
        return redirect(url_for('home'))

class SignIn(MethodView):
    def post(self):
        logger.debug(request.form)
        form = LoginForm(request.form)
        ret = {'code' : form.FAILED}
        user = User.query.filter_by(username = form.login_username.data).first()
        if user and check_password_hash(user.password, form.login_password.data):
            login_user(user)
            ret['code'] = form.SUCCESS
        return json.dumps(ret)

class ChangePassword(MethodView):
    def get(self):
        form = ChangePasswordForm(request.form)
        return render_template('/passport/change_password.html', form=form)

    def post(self):
        form = ChangePasswordForm(request.form)
        if form.validate():
            if not check_password_hash(current_user.password, form.current_password.data):
                flash(u'密码错误')
            else:
                current_user.password = generate_password_hash(form.new_password.data)
                dbs.session.commit()
                flash(u'修改成功')
                return redirect(url_for('home'))
        return render_template('/passport/change_password.html', form=form)




