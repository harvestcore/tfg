from flask import request
from flask_restplus import Resource, Namespace
from marshmallow import fields, Schema, validate

from src.classes.user import User
from src.utils.validate_or_abort import validate_or_abort
from src.utils.parse_data import parse_data
from src.utils.response_by_success import response_by_success

# GET, POST, DELETE
api = Namespace(name='user', description='User management')


class UserSchema(Schema):
    type = fields.Str(required=True,
                      validate=validate.OneOf(["admin", "regular"]))
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True)
    enabled = fields.Bool(dump_only=True)
    deleted = fields.Bool(dump_only=True)
    # creation_time = fields.DateTime(dump_only=True)
    # last_modified = fields.DateTime(dump_only=True)
    # delete_time = fields.DateTime(dump_only=True)


class UserSchemaQuery(Schema):
    query = fields.Dict(required=True)
    filter = fields.Dict()


class UserSchemaPut(Schema):
    email = fields.Str(required=True)
    data = fields.Nested(UserSchema, required=True)


class UserSchemaDelete(Schema):
    email = fields.Str(required=True)


@api.route('/<string:username>')
class UserServiceGet(Resource):
    @staticmethod
    def get(username):
        user = User().find(criteria={'username': username})
        return {'payload': username, 'user': user.data}


@api.route('/query')
class UserServiceGetWithQuery(Resource):
    @staticmethod
    def post():
        data = validate_or_abort(UserSchemaQuery, request.get_json())
        user = User().find(criteria=data['query'],
                           projection=data['filter'] if 'filter' in data.keys()
                           else {})

        return parse_data(UserSchema, user.data)


@api.route('/')
class UserService(Resource):
    @staticmethod
    def post():
        data = validate_or_abort(UserSchema, request.get_json())
        return response_by_success(User().insert(data))

    @staticmethod
    def put():
        data = validate_or_abort(UserSchemaPut, request.get_json())
        return response_by_success(User().update(criteria={
            'email': data['email']
        }, data=data['data']))

    @staticmethod
    def delete():
        data = validate_or_abort(UserSchemaDelete, request.get_json())
        return response_by_success(User().remove(criteria={
            'email': data['email']
        }), is_remove=True)
