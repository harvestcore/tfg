from flask import request, make_response
from flask_restplus import Resource, Namespace
from marshmallow import fields, Schema
from functools import wraps

from src.classes.login import Login
from src.utils.parse_data import parse_data
from src.utils.response_by_success import response_by_success
from src.utils.response_with_message import response_with_message

# GET, POST, DELETE
api = Namespace(name='login', description='Login')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return response_with_message(message="Token is missing", code=401)

        current_user = Login().token_access(str(token))

        if current_user.data is None:
            return response_with_message(message="Invalid token", code=401)

        return f(*args, **kwargs)

    return decorated


class LoginSchema(Schema):
    token = fields.Str(dump_only=True)


@api.route('/')
class LoginService(Resource):
    @staticmethod
    def get():
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response(
                'Could not verify.',
                401,
                {'WWW-Authenticate': 'Basic realm="Login required."'}
            )

        login = Login().login(auth)

        if not login:
            return response_by_success(False)

        return parse_data(LoginSchema, login.data)


@api.route('/logout')
class LogoutService(Resource):

    @staticmethod
    @token_required
    def get():
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        current_user = Login().token_access(str(token))
        return response_by_success(
            Login().logout(current_user.data['username'])
        )
