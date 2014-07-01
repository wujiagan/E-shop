#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from jing.core.database import dbs
    

#库存
class Inventory(dbs.Model):
    STATUS_INBOUND = 2 
    STATUS_OUTBOUND = 4
    STATUS = {
              STATUS_INBOUND: u'入库'
              , STATUS_OUTBOUND: u'出库'
              }
    __tablename__ = 'inventory'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(256))
    number = dbs.Column(dbs.Integer())
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('user.id'))
    goods_id = dbs.Column(dbs.Integer, dbs.ForeignKey('goods.id'))
    order_id = dbs.Column(dbs.Integer, dbs.ForeignKey('order.id'))
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now)
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer(), nullable = False)
    
    def __unicode__(self):
        return self.name