#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jing.core.database import dbs

class Address(dbs.Model):
    __tablename__ = 'address'
    id = dbs.Column(dbs.Integer, primary_key=True)
    name = dbs.Column(dbs.String(128), nullable = False)
    mobile_phone = dbs.Column(dbs.String(16), nullable = False)
    address = dbs.Column(dbs.String(255), nullable = False)
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.mobile_phone = kwargs.pop('mobile_phone', None)
        self.address = kwargs.pop('address', None)
        self.user_id = kwargs.pop('user_id', None)
        
    def __unicode__(self):
        return self.name