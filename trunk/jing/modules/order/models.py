#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from jing.core.database import dbs
    

# Define models
goods_order = dbs.Table('goods_order',
        dbs.Column('order_id', dbs.Integer(), dbs.ForeignKey('order.id')),
        dbs.Column('goods_id', dbs.Integer(), dbs.ForeignKey('goods.id')))


class Order(dbs.Model):
    STATUS_DRAFT = 0
    STATUS_PAYING = 3
    STATUS_DELIVERING = 6
    STATUS_SUCCESS = 9
    STATUS_ABORT = 12
    STATUS = {
              STATUS_DRAFT: u'未确认'
              , STATUS_PAYING: u'已提交'
              , STATUS_DELIVERING: u'支付中'
              , STATUS_SUCCESS: u'已支付'
              , STATUS_ABORT: u'已取消'
              }
    __tablename__ = 'order'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(128)) #收货人
    user_id = dbs.Column(dbs.Integer, dbs.ForeignKey('user.id'))
    amount = dbs.Column(dbs.Float, default=0.0) #金额
    
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now) #下单时间
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer(), nullable = False, default = STATUS_DRAFT)
    
    goods = dbs.relationship('Goods', secondary=goods_order,
                            backref=dbs.backref('order', lazy='dynamic'))
    payments = dbs.relationship('Payment', backref = 'order', lazy = 'dynamic')
    
    def __unicode__(self):
        return self.name