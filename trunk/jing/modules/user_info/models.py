#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jing.core.database import dbs


class UserInfo(dbs.Model):
    __tablename__ = 'user_info'
    id = dbs.Column(dbs.Integer, primary_key=True)
    full_name = dbs.Column(dbs.Unicode(10))
    birthday = dbs.Column(dbs.DateTime)
    mobile_phone = dbs.Column(dbs.String(16))
    email = dbs.Column(dbs.String(126))
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('user.id'))

    def __unicode__(self):
        return self.full_name