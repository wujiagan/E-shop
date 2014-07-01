# coding: utf-8
import os
from flask import send_from_directory, current_app, request
from flask.ext.security import roles_accepted

from ..core.views import PageHome
from ..modules.captcha.views import GenPic, CheckPic, CheckPicJ, CheckPicJCB
from ..modules.passport.views import Register, SignIn, Logout, ChangePassword, IsRegistered
from ..modules.sms.views import SendSMS
from ..modules.address.views import *
from ..modules.user_info.views import Index as UserInfo
from ..modules.manage.views import (UserList as ManageUserList , UserDetail as ManageUserDetail, 
    GoodsList as ManageGoodsList, GoodsDetail as ManageGoodsDetail, GoodsAdd as ManageGoodsAdd, )
from ..modules.goods.views import *
from ..modules.order.views import *
from ..modules.payment.views import *
from ..modules.channel.views import *
from ..modules.inventory.views import *
from ..modules.usercenter.views import *



def configure(app):
    app.add_url_rule('/', view_func=PageHome.as_view('home'))
    
    app.add_url_rule('/captcha/gen_pic', view_func=GenPic.as_view('gen_pic'),)
    app.add_url_rule('/captcha/check_pic', view_func=CheckPic.as_view('check_pic'),)
    app.add_url_rule('/captcha/check_pic_j', view_func=CheckPicJ.as_view('check_pic_j'),)
    app.add_url_rule('/captcha/check_pic_jcb', view_func=CheckPicJCB.as_view('check_pic_jcb'),)
    
    app.add_url_rule('/Users/checkuser', view_func=IsRegistered.as_view('passport_is_registered'),)
    app.add_url_rule('/Users/register', view_func=Register.as_view('passport_register'),)
    app.add_url_rule('/Users/login', view_func=SignIn.as_view('passport_signin'),)
    app.add_url_rule('/Users/logout', view_func=Logout.as_view('passport_logout'),)
    app.add_url_rule('/passport/change_password', view_func=ChangePassword.as_view('passport_change_password'),)

    app.add_url_rule('/sms/send', view_func=SendSMS.as_view('send_sms'),)
    
    app.add_url_rule('/user_info/index', view_func=UserInfo.as_view('user_info'),)
    
    
    app.add_url_rule('/Usercenter/orders', view_func=UsercenterOrders.as_view('usercenter_orders'),)
    
    

    ''' 后台管理模块 start'''    
    app.add_url_rule('/manage/', view_func=ManageUserList.as_view('manage'),)
    app.add_url_rule('/manage/user_list', view_func=ManageUserList.as_view('manage_user_list'),)
    app.add_url_rule('/manage/user_detail/<path:user_id>', view_func=ManageUserDetail.as_view('manage_user_detail'),)
    
    app.add_url_rule('/manage/goods_list', view_func=ManageGoodsList.as_view('manage_goods_list'),)
    app.add_url_rule('/manage/goods_add', view_func=ManageGoodsAdd.as_view('manage_goods_add'),)
    
    ''' 后台管理模块 end'''
        
    app.add_url_rule('/media/<path:filename>', view_func=media)
    app.add_url_rule('/template_files/<path:filename>',
                     view_func=template_files)

    for filepath in app.config.get('MAP_STATIC_ROOT', []):
        app.add_url_rule(filepath, view_func=static_from_root)


@roles_accepted('admin', 'developer')
def template_files(filename):
    template_path = os.path.join(current_app.root_path,
                                 current_app.template_folder)
    return send_from_directory(template_path, filename)

def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)

def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])

