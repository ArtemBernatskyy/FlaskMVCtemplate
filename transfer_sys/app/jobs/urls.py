from flask import Blueprint
# thir party
from flask_restful import Api
# local
from .views import JobList, JobCreate, JobDetail, JobFileDetail


blueprint = Blueprint('jobs', __name__)
api = Api(blueprint)

api.add_resource(JobList, '/')
