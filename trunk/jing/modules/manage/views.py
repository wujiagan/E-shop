# -*- coding: utf-8 -*-
from ..passport.models import User, Role
from flask import request, redirect, url_for, Response, session
from flask.views import MethodView
from flask_security.decorators import roles_accepted
from jing.core.templates import render_template
from jing.modules.goods.models import Goods
import logging

logger = logging.getLogger()

'''会员管理'''
class UserList(MethodView):
    @roles_accepted('editor', 'admin')
    def get(self):
        member = Role.query.filter_by(name='member').first()
        users = User.query.filter(User.roles.contains(member)).all()
        return render_template('manage/user/list.html', users=users)
    
class UserDetail(MethodView):
    @roles_accepted('editor', 'admin')
    def get(self, user_id):
        user = User.query.get(user_id)
        return render_template('manage/user/detail.html', user=user)
    
''' 商品管理'''
    
class GoodsList(MethodView):
    @roles_accepted('editor', 'admin')
    def get(self):
        goods_list = Goods.query.all()
        return render_template('manage/goods/list.html', goods_list=goods_list)
    
class GoodsDetail(MethodView):
    @roles_accepted('editor', 'admin')
    def get(self, goods_id):
        goods = Goods.query.get(goods_id)
        return render_template('manage/goods/detail.html', goods=goods)
    
class GoodsAdd(MethodView):
    @roles_accepted('editor', 'admin')
    def get(self):
        return render_template('manage/goods/add.html')
    
