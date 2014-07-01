# -*- coding: utf-8 -*-
from jing import admin
from .models import Address
from jing.core.database import dbs
from flask.ext.admin.contrib import sqla

admin.add_view(sqla.ModelView(Address, dbs.session, name=u"地址", category=u'用户管理'))


