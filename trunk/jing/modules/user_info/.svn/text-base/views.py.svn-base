# -*- coding: utf-8 -*-
from ...utils import password
from ...utils.captcha.pic_checker import PicChecker
from flask import request, redirect, url_for, Response, session
from flask.views import MethodView
from flask_security.decorators import roles_accepted
import logging


try:
    import cStringIO as StringIO
except:
    import StringIO

logger = logging.getLogger()

class Index(MethodView):
    @roles_accepted('member')
    def get(self):
        return 'myinfo'
    
