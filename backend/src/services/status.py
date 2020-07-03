from flask import request
from flask_restplus import Resource, Namespace

from src.classes.docker_engine import DockerEngine
from src.classes.login import Login
from src.classes.mongo_engine import MongoEngine
from src.classes.user import User
from src.services.login import token_required


api_status = Namespace(name='status', description='Status')
api_healthcheck = Namespace(name='api/healthcheck', description='Health Check')


@api_status.route('')
class StatusService(Resource):

    @staticmethod
    @token_required
    def get():
        user = Login().get_username(request.headers['x-access-token'])
        is_admin = User().is_admin(user)

        return {
            'mongo': MongoEngine().status(is_admin),
            'docker': DockerEngine().status()
        }, 200


@api_healthcheck.route('')
class StatusService(Resource):

    @staticmethod
    def get():
        mongo = MongoEngine().status()
        docker = DockerEngine().status()
        hc = mongo['is_up'] and docker['is_up']
        code = 200 if hc else 500
        return {
            'ok': hc
        }, code
