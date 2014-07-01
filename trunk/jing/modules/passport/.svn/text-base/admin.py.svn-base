# -*- coding: utf-8 -*-
from jing import admin
from .models import Role, User
from jing.core.database import dbs
from flask.ext.admin.contrib import sqla

class UserAdmin(sqla.ModelView):
    column_list = ('username', 'email', 'active',
                   'last_login_at', 'login_count')

class RoleAdmin(sqla.ModelView):
    column_list = ('name', 'description')

admin.add_view(UserAdmin(User, dbs.session, name=u"用户", category=u'用户管理'))
admin.add_view(RoleAdmin(Role, dbs.session, name=u"角色", category=u'用户管理'))


