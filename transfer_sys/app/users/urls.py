from flask import Blueprint
# thir party
from flask_restful import Api
# local
from .views import CheckToken


blueprint = Blueprint('users', __name__)
api = Api(blueprint)

api.add_resource(CheckToken, '/')
