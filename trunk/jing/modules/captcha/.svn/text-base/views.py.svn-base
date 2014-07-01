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

CAPTCHA_NAME='captcha_no'

class GenPic(MethodView):
    def get(self):
        captcha_no = password.gen_salt(4).upper()
        captcha_no = captcha_no.replace('0','2')
        captcha_no = captcha_no.replace('1','3')
        captcha_no = captcha_no.replace('O','A')
        captcha_no = captcha_no.replace('I','B')
        captcha_no = captcha_no.replace('J','X')
        session[CAPTCHA_NAME] = captcha_no
#        pic_checker=PicChecker(fonttype = config['captcha_font_path'], size=(85, 24), fontsize=18) 
        pic_checker=PicChecker(size=(85, 24), fontsize=18) 
        im = pic_checker.createChecker(captcha_no)
        from flask import make_response
        output = StringIO.StringIO()
        im.save(output,"GIF")
        img_data = output.getvalue()
        output.close()
        response = make_response(img_data)
        response.headers['Content-Type'] = 'image/gif'
        return response

class CheckPic(MethodView):
    def get(self):    
        captcha_no = request.args.get(CAPTCHA_NAME, '')
        cmp_rst = cmp(str(captcha_no).lower(),str(session[CAPTCHA_NAME]).lower())
        tmp = str(captcha_no).lower() + '---' + str(session[CAPTCHA_NAME]).lower() + ':' + str(cmp_rst)
        print(tmp)
        if cmp_rst:
            return 'false'
        else:
            return 'true'

class CheckPicJ(MethodView):
    def get(self):    
        result = 'true'
        captcha_no = request.args.get(CAPTCHA_NAME)
        cmp_rst = cmp(str(captcha_no).lower(),str(session[CAPTCHA_NAME]).lower())
        if cmp_rst:
            result = 'false'
        cb_name = request.args.get('jsoncallback')
        return '%s({"result": "%s"})' % (cb_name, result)    

class CheckPicJCB(MethodView):
    def get(self): 
        result = 'true'
        captcha_no = request.args.get(CAPTCHA_NAME)
        cmp_rst = cmp(str(captcha_no).lower(),str(session[CAPTCHA_NAME]).lower())
        if cmp_rst:
            result = 'false'
        cb_name = request.args.get('jsoncallback')
        return '%s(%s)' % (cb_name, result)
