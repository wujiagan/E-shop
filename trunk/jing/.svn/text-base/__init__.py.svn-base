#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from .core.app import jingFlask  # Flask with custom template loader

import logging
logger = logging.getLogger()

try:
    from .core.admin import create_admin
    admin = create_admin()
except:
    # Fix setup install:
    # If new environment not return error
    pass


def create_app(config=None, test=False, admin_instance=None, **settings):
    app = jingFlask('jing')
    app.config.from_envvar("APP_SETTINGS", silent=True)
    
    app.config.from_object('jing.settings')
    
    if config:
        app.config.from_pyfile(config)

    # Settings from mode
    mode = os.environ.get('MODE')
    if mode:
        app.config.from_object('jing.%s_settings' % mode)

    # Local settings
    if not test:
        app.config.from_pyfile(
            os.path.join(os.path.dirname(__file__), 'local_settings.py'),
            silent=True
        )

    # Overide settings
    app.config.update(settings)

    # with app.test_request_context():
    from .ext import configure_extensions
    configure_extensions(app, admin)

    # app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
    return app


def create_api(config=None, **settings):
    return None


def create_celery_app(app=None):
    from celery import Celery
    app = app or create_app()
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
