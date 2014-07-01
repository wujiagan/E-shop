# coding: utf-8

from flask.views import MethodView
from jing.core.templates import render_template
import logging

logger = logging.getLogger()

class PageHome(MethodView):
    def get(self, param = None):
        return render_template('index.html')

