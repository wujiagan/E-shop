#coding: utf-8
import os

"""
the get_password function tries to find a file called
<arg>_password.txt containing the txt.

By default it looks in application root folder parent.

get_password('db') - > ../db_password.txt

Import it if you want to pass some password to your configs.
"""
# from jing.utils.settings import get_password


"""
DB for localhost
"""

"""
DB in remote host
- register for free in mongolab.com
"""
# MONGODB_SETTINGS = {'DB': "jing",
#                     'USERNAME': 'jing',
#                     'PASSWORD': get_password('db'),
#                     'HOST': 'ds035498.mongolab.com',
#                     'PORT': 35498}

"""
This should really be secret for security
use os.random, urandom or uuid4 to generate
in your shell
$ python -c "import uuid;print uuid.uuid4()"
then use the generated key
"""
SECRET_KEY = "KeepThisS3cr3t"

"""
Take a look at Flask-Cache documentation
"""
CACHE_TYPE = "simple"


"""
Not needed by flask, but those root folders are used
by FLask-Admin file manager
"""
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

"""
Files on MAP_STATIC_ROOT will be served from /static/
example: /static/favicon.ico will be served by site.com/favicon.ico
"""
MAP_STATIC_ROOT = ('/robots.txt', '/sitemap.xml', '/favicon.ico')


"""
If enabled admin will leave creation of repeated slugs
but will append a random int i.e: blog-post-2342342
"""
SMART_SLUG_ENABLED = False

"""
Blueprints are jing-modules, you don't need to install
just develop or download and drop in your modules folder
by default it is in /modules, you can change if needed
"""
BLUEPRINTS_PATH = 'modules'
BLUEPRINTS_OBJECT_NAME = 'module'

"""
Default configuration for FLask-Admin instance
:name: - will be the page title
:url: - is the ending point
"""
ADMIN = {'name': u'后台管理', 'url': '/admin'}

"""
File admin can expose folders, you just need to have them
mapped in your server or in flask, see quooka.ext.views
"""

"""
This is for Flask-Collect extension
you can install blueprints with static files and run
python manage.py collectstatic to copy to main static folder
"""
COLLECT_STATIC_ROOT = STATIC_ROOT

"""
Never change it here, use local_settings for this.
"""
MODE = 'production'
DEBUG = False

"""
Debug toolbar only works if installed
pip install flask-debugtoolbar
"""
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_PROFILER_ENABLED = True
DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
DEBUG_TB_PANELS = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
)

"""
By default DEBUG_TOOLBAR is disabled
do not change it here, do it in local_settings.py
DEBUG_TOOLBAR_ENABLED = True
"""
DEBUG_TOOLBAR_ENABLED = False


"""
Flask-Gravatar can take avatar urls in jinja templates
do: {{ current_user.email | gravatar }} or
{{ 'some@server.com' | gravatar(size=50) }}
"""
GRAVATAR = {
    'size': 100,
    'rating': 'g',
    'default': 'retro',
    'force_default': False,
    'force_lower': False
}

"""
Emails go to shell until you configure this
http://pythonhosted.org/Flask-Mail/

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
# MAIL_USE_SSL = True
MAIL_USE_TLS = True
MAIL_USERNAME = 'rochacbruno@gmail.com'
# Create a .email_password.txt in ../
MAIL_PASSWORD = get_password('email')
DEFAULT_MAIL_SENDER = None
"""


MAIL_SERVER = "smtp.exmail.qq.com"
MAIL_USERNAME = "dev-sender@fn315.com"
MAIL_PASSWORD = "xsw23EDC"

"""
Take a look at Flask-Security docs
http://pythonhosted.org/Flask-Security/configuration.html
"""
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_URL_PREFIX = '/accounts'
SECURITY_PASSWORD_SALT = '6e95b1ed-a8c3-4da0-8bac-6fcb11c39ab4'
SECURITY_EMAIL_SENDER = 'dev-sender@fn315.com'
SECURITY_REGISTERABLE = False
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True
SECURITY_TRACKABLE = True


"""
Dealer can versionate static files if you are under a repo
in most cases you dont need to change this config
in templates you can do
<script src="{{ url_for('static', filename='xxx.js')}}?version={{revision}}" >
:revision: is the latest commit in the repository for this file.
"""
DEALER_PARAMS = dict(
    backends=('git', 'mercurial', 'simple', 'null')
)


"""
Internationalization for Flask-Admin
if want to use in your site home page, read babel docs.
"""
# BABEL_DEFAULT_LOCALE = 'en'
# BABEL_DEFAULT_LOCALE = 'zh_CN'
BABEL_DEFAULT_LOCALE = 'zh'


# WTForms
CSRF_ENABLED = True
"""
It is good to use uuid here
$ python -c "import uuid;print uuid.uuid4()"
"""
CSRF_SESSION_KEY = "somethingimpossibletoguess"


DEFAULT_THEME = 'default'
DEBUG = True

DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
DATABASE_USER = 'jing'
DATABASE_PWD = 'jing'
DATABASE_NAME = 'jing'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql://'+DATABASE_USER+':'+DATABASE_PWD+'@'+DATABASE_HOST+':'+DATABASE_PORT+'/'+DATABASE_NAME+'?charset=utf8'

"""
It configures the default logger for app instance
"""
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d.%m %H:%M:%S')
logging.info("Core settings loaded.")
