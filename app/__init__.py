from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from .resources import init_api


def create_app():
    app = Flask(__name__)
    # ProxyFixとは？
    app.wsgi_app = ProxyFix(app.wsgi_app)
    init_api(app)
    return app
