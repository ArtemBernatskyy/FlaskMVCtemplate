from bson.errors import InvalidId
from bson.objectid import ObjectId
from werkzeug import secure_filename
from flask import request, url_for, make_response
# third party
from gridfs.errors import NoFile
from flask_restful import Resource, abort
# local imports
from .models import Job


class JobList(Resource):
    def get(self):
        files = [file for file in Job.objects]
        context = {
            file.title: url_for('tasks.task_detail', id=str(file.id)) for file in files
        }
        return context
