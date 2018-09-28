from flask import Flask
from app.main.controller.v1 import API_V1
from .extensions import db, bcrypt
from .config import config_by_name

__all__ = ['create_app']


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config.SWAGGER_UI_REQUEST_DURATION = True
    app.register_blueprint(API_V1.blueprint)
    db.init_app(app)
    bcrypt.init_app(app)

    return app
