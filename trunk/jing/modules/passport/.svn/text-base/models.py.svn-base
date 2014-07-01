#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.security import UserMixin, RoleMixin
from flask.ext.security.utils import encrypt_password

from jing.core.database import dbs
from ..user_info.models import UserInfo
from ..address.models import Address
from ..order.models import Order

# Define models
roles_users = dbs.Table('roles_users',
        dbs.Column('user_id', dbs.Integer(), dbs.ForeignKey('user.id')),
        dbs.Column('role_id', dbs.Integer(), dbs.ForeignKey('role.id')))

class Role(dbs.Model, RoleMixin):
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(80), unique=True)
    description = dbs.Column(dbs.String(255))
    
    @classmethod
    def create(self, name, description=None):
        role = Role()
        role.name = name
        role.description = description
        dbs.session.add(role)
        dbs.session.commit()
        return role
    
    def __unicode__(self):
        return self.name

class User(dbs.Model, UserMixin):
    id = dbs.Column(dbs.Integer, primary_key=True)
    email = dbs.Column(dbs.String(255), unique=True)
    password = dbs.Column(dbs.String(255))
    active = dbs.Column(dbs.Boolean(), default=True)
    confirmed_at = dbs.Column(dbs.DateTime())
    roles = dbs.relationship('Role', secondary=roles_users,
                            backref=dbs.backref('users', lazy='dynamic'))
    addresses = dbs.relationship('Address', backref = 'user', lazy = 'dynamic')
    orderes = dbs.relationship('Order', backref = 'user', lazy = 'dynamic')
    user_info = dbs.relationship('UserInfo', backref = 'user', lazy = 'dynamic')
    last_login_at = dbs.Column(dbs.DateTime)
    current_login_at = dbs.Column(dbs.DateTime)
    last_login_ip = dbs.Column(dbs.String(255))
    current_login_ip = dbs.Column(dbs.String(255))
    login_count = dbs.Column(dbs.Integer)
    username = dbs.Column(dbs.String(50), unique=True, nullable = False)

    def is_active(self):
        return self.active
    
    def is_admin(self):
        roles = self.roles
        for role in roles:
            if role.name == 'admin':
                return True
        return False

    def __unicode__(self):
        return self.email