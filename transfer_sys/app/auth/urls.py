from flask import Blueprint
# thir party
from flask_restful import Api
# local
from .views import LoginView


blueprint = Blueprint('auth', __name__)
api = Api(blueprint)

api.add_resource(LoginView, '/login/', endpoint='login')
