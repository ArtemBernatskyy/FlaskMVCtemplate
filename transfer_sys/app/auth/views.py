from flask import request
# third party
from flask_restful import Resource, abort
# local
from .utils import generate_jwt, verify_password


class LoginView(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        check_pass = verify_password(username, password)
        if check_pass:
            jwt_roken = generate_jwt(check_pass.username)
            context = {
                'token': jwt_roken
            }
            return context
        else:
            abort(401, description="Wrong credentials !")
