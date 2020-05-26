from flask import request
from flask_restplus import Resource, Namespace

from src.classes.login import Login
from src.classes.user import User
from src.services.login import token_required
from src.schemas.common import QuerySchema
from src.schemas.user import UserSchema, UserSchemaDelete, UserSchemaPut
from src.utils.validate_or_abort import validate_or_abort
from src.utils.parse_data import parse_data
from src.utils.response_by_success import response_by_success


api = Namespace(name='user', description='User management')


@api.route('/<string:username>')
class UserServiceGet(Resource):
    @staticmethod
    @token_required
    def get(username):
        user = User().find(criteria={'username': username})
        return parse_data(UserSchema, user.data)


@api.route('/query')
class UserServiceGetWithQuery(Resource):
    @staticmethod
    @token_required
    def post():
        data = validate_or_abort(QuerySchema, request.get_json())
        user = User().find(
            criteria=data['query'],
            projection=data['filter'] if 'filter' in data.keys() else {}
        )

        return parse_data(UserSchema, user.data)


@api.route('')
class UserService(Resource):
    @staticmethod
    @token_required
    def get():
        username = Login().get_username(request.headers['x-access-token'])
        user = User().find({'username': username})
        return parse_data(UserSchema, user.data) if user and user.data \
            else response_by_success(False)

    @staticmethod
    @token_required
    def post():
        data = validate_or_abort(UserSchema, request.get_json())
        return response_by_success(User().insert(data))

    @staticmethod
    @token_required
    def put():
        data = validate_or_abort(UserSchemaPut, request.get_json())
        return response_by_success(User().update(criteria={
            'email': data['email']
        }, data=data['data']))

    @staticmethod
    @token_required
    def delete():
        data = validate_or_abort(UserSchemaDelete, request.get_json())
        return response_by_success(User().remove(criteria={
            'email': data['email']
        }), is_remove=True)
