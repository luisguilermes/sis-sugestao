# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.sugestao_controller import api as sugestao_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='')

api.add_namespace(sugestao_ns, path='/sugestao')