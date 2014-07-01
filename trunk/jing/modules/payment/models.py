#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from jing.core.database import dbs
    

class Payment(dbs.Model):
    __tablename__ = 'payment'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(128))
    order_id = dbs.Column(dbs.Integer, dbs.ForeignKey('order.id'))
    money = dbs.Column(dbs.Float, default=0.0)
    channel_id =  dbs.Column(dbs.Integer, dbs.ForeignKey('channel.id')) #支付渠道
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now)
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer(), nullable = False)

    def __unicode__(self):
        return self.name