# -*- coding: utf-8 -*-
from jing import admin
from .models import *
from jing.core.database import dbs
from flask.ext.admin.contrib.sqla import ModelView


admin.add_view(ModelView(Order, dbs.session, name=u"订单", category=u'订单支付'))


