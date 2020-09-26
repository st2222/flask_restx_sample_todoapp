from .TodoAPI import ns
from flask_restx import Api
from flask import Blueprint


api_bp = Blueprint('api', __name__, url_prefix=None)

api = Api(api_bp, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )
api.add_namespace(ns)


def init_api(app):
    app.register_blueprint(api_bp)
