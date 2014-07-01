# -*- coding: utf-8 -*-
from jing import admin
from .models import *
from jing.core.database import dbs
from flask.ext.admin.contrib.sqla import ModelView


admin.add_view(ModelView(Inventory, dbs.session, name=u"库存", category=u'库存管理'))


