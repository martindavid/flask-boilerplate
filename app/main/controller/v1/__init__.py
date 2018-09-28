from flask import Blueprint
from flask_restplus import Api
from .todo import api as todo_api

API_V1 = Api(
    Blueprint('api_v1', __name__, url_prefix='/v1'),
    title='Flask boilerplate API',
    version='1.0',
    description='Documentation for Flask boilerplate API',
)

API_V1.namespaces.clear()
API_V1.add_namespace(todo_api)
