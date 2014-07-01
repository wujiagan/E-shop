# -*- coding: utf-8 -*-
from jing import admin
from .models import *
from jing.core.database import dbs
from flask.ext.admin.contrib.sqla import ModelView


admin.add_view(ModelView(Category, dbs.session, name=u"分类", category=u'商品管理'))
admin.add_view(ModelView(Goods, dbs.session, name=u"商品", category=u'商品管理'))


