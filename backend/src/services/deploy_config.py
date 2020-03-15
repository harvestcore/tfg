from flask_restplus import Namespace, Resource

# GET, POST, DELETE
api = Namespace(name='deploy-config', description='Deploy-config management')


@api.route('/')
class DeployConfigService(Resource):
    def get(self):
        return {'get': 'get', 'a': 1}

    def post(self):
        return {'post': 'post', 'a': 1}

    def put(self):
        return {'put': 'put', 'a': 1}

    def delete(self):
        return {'delete': 'delete', 'a': 1}, 204