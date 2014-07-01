# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, Response, session
from flask.views import MethodView
from flask_security.decorators import roles_accepted
import logging

logger = logging.getLogger()

from ...core.templates import render_template

from ..order.models import Order

class UsercenterOrders(MethodView):
    @roles_accepted('admin', 'member')
    def get(self):
        orders = Order.query.all()
#        return render_template('manage/goods/list.html', goods_list=goods_list)
        return render_template('usercenter/orders.html', orders = orders)
    
