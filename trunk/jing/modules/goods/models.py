#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from jing.core.database import dbs
    
class Category(dbs.Model):
    __tablename__ = 'category'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(128), unique=True)
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now)
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer, nullable=False, default=1)
    parent_id = dbs.Column(dbs.Integer, dbs.ForeignKey('category.id'))
    children = dbs.relationship("Category",
        backref=dbs.backref('category', remote_side=[id])
    )
    goods = dbs.relationship('Goods', backref = 'category', lazy = 'dynamic')

    def __unicode__(self):
        return self.name

class Goods(dbs.Model):
    __tablename__ = 'goods'
    id = dbs.Column(dbs.Integer(), primary_key=True)
    name = dbs.Column(dbs.String(128))
    category_id = dbs.Column(dbs.Integer, dbs.ForeignKey('category.id'))
    
    create_time = dbs.Column(dbs.DateTime, default=datetime.datetime.now)
    update_time = dbs.Column(dbs.DateTime)
    status = dbs.Column(dbs.Integer, nullable=False, default=1)
    weight = dbs.Column(dbs.Integer, default=0)
    spec = dbs.Column(dbs.String(32), default=None)
    production_date = dbs.Column(dbs.Date)
    overdue_date = dbs.Column(dbs.Date)
    price = dbs.Column(dbs.Integer, nullable=False, default=0)
    inventories = dbs.relationship('Inventory', backref = 'goods', lazy = 'dynamic')
    def __unicode__(self):
        return self.name

