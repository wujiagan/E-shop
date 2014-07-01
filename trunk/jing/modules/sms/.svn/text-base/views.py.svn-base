# -*- coding: utf-8 -*-
from flask import request, redirect, render_template, url_for, Response, session
from flask.views import MethodView

from ...utils import password
from ...utils.captcha.pic_checker import PicChecker

try:
    import cStringIO as StringIO
except:
    import StringIO

import logging
logger = logging.getLogger()


class SendSMS(MethodView):
    def get(self):
        content = u'%s【尚田农品】' % (u'尚田农品会员招募中，免费体验无公害蔬菜送货上门服务，你还在犹豫什么呢？')
        return sendSMS('15322371085', content.encode('gb2312') )
    
    def post(self):
        return 'sms'
    
import time
def sendSMS(mobile, content):
    sms_id = 'fn315'
    pwd = '445566'
    
    url = "http://service.winic.org:8009/sys_port/gateway/?id=%s&pwd=%s&to=%s&content=%s&time=%s" % \
        (sms_id, pwd, mobile, content, time.time())
        
    import urllib2
    response = urllib2.urlopen(url)
    return response.read()

