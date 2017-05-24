# third party
from flask_restful import Resource
# local
from app.auth.utils import auth


class CheckToken(Resource):
    @auth.login_required
    def get(self):
        context = {
            'ctx': "hello secret"
        }
        return context
