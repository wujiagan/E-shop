# coding: utf-8
from flask.ext.mail import Mail
from flask.ext.cache import Cache
from flask.ext.security import Security, SQLAlchemyUserDatastore

from dealer.contrib.flask import Dealer
from jing.core.database import dbs
from jing.core.admin import configure_admin

from jing.modules.passport.models import Role, User

from . import (babel, blueprints, error_handlers, context_processors,
               before_request, views, themes, fixtures)

def configure_extensions(app, admin):
    babel.configure(app)
    Cache(app)
    Mail(app)
    error_handlers.configure(app)
    dbs.init_app(app)
    fixtures.configure(app)
    themes.configure(app)  # Themes should be configured after db
    
    user_datastore = SQLAlchemyUserDatastore(dbs, User, Role)
    Security(app, user_datastore)
    configure_admin(app, admin)
    blueprints.load_from_folder(app)

    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(app)
        except:
            pass

    before_request.configure(app)
    views.configure(app)
    return app
