from flask_restplus import Namespace, Resource

# GET, POST, DELETE
api = Namespace(name='deploy', description='Deploy management')


@api.route('/')
class DeployService(Resource):
    def get(self):
        return {'get': 'get', 'a': 1}

    def post(self):
        return {'post': 'post', 'a': 1}

    def put(self):
        return {'put': 'put', 'a': 1}

    def delete(self):
        return {'delete': 'delete', 'a': 1}, 204
