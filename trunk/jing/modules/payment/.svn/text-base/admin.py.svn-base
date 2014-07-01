# -*- coding: utf-8 -*-
from jing import admin
from .models import *
from jing.core.database import dbs
from flask.ext.admin.contrib.sqla import ModelView


admin.add_view(ModelView(Payment, dbs.session, name=u"支付", category=u'订单支付'))


