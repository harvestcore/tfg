from flask_restplus import Namespace, Resource
from marshmallow import fields

# GET, POST, DELETE
api = Namespace(name='client', description='Client management')


class ClientSchema:
    name = fields.String()
    id = fields.String()


@api.route('/<int:id>')
class ClientService(Resource):
    def get(self, id):
        return {'payload': id}


@api.route('/')
class ClientService(Resource):
    def post(self):
        return {'payload': api.payload}

    def put(self):
        return {'payload': api.payload}

    def delete(self):
        return {'payload': api.payload}
