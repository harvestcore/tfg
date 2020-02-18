from flask_restplus import Namespace, Resource
from src.classes.user import User
from src.classes.customer import Customer

# GET, POST, DELETE
api = Namespace(name='user', description='User management')


@api.route('/<string:username>')
class UserServiceGet(Resource):
    @staticmethod
    def get(username):
        user = User().find(criteria={'username': username})
        return {'payload': username, 'user': user.data}


@api.route('/')
class UserService(Resource):
    def get(self):
        user = User().find()
        return {'post': 'get', 'result': user.data}

    def post(self):
        user = User()
        data = user.insert(data=api.payload)
        return {'post': 'post', 'result': data}

    def put(self):
        data = User().update(item=api.payload['username'],
                             data=api.payload['data'])
        return {'put': 'put', 'result': data}

    def delete(self):
        user = User()
        payload = api.payload
        data = user.remove(payload)
        return {'delete': 'delete', 'data': data}, 204
