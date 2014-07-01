#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from jing.core.database import dbs
    
class Channel(dbs.Model):
    __tablename__ = 'channel'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(128))
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now)
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer(), nullable = False)
    payments = dbs.relationship('Payment', backref = 'channel', lazy = 'dynamic')

    def __unicode__(self):
        return self.name