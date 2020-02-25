from flask import request
from flask_restplus import Namespace, Resource

from src.classes.docker_engine import DockerEngine
from src.services.login import token_required
from src.utils.response_by_success import response_by_success
from src.utils.validate_or_abort import validate_or_abort
from src.utils.container_operation_schemas import *
from src.utils.parse_data import parse_data

# GET, POST, DELETE
api = Namespace(name='deploy', description='Deploy management')


@api.route('/container/single')
class DeployService(Resource):
    @staticmethod
    def post():
        payload = validate_or_abort(BaseSingleContainerProps,
                                    request.get_json())
        container = DockerEngine().get_container_by_id(payload['container_id'])
        if container:
            response = DockerEngine().run_operation_in_container(
                container=container,
                operation=payload['operation'],
                data=payload['data']
            )

            if response is not False:
                return parse_data(None, response)

        return response_by_success(False)


@api.route('/container')
class DeployService(Resource):
    @staticmethod
    def post():
        payload = validate_or_abort(BaseContainersProps, request.get_json())
        data = payload['data']

        if payload['operation'] == 'run':
            payload['data'] = validate_or_abort(ContainersRunProps, data)
            payload['data']['detach'] = True

        if payload['operation'] == 'get':
            payload['data'] = validate_or_abort(ContainersGetProps, data)

        if payload['operation'] == 'list':
            payload['data'] = validate_or_abort(ContainersListProps, data)

        if payload['operation'] == 'prune':
            payload['data'] = validate_or_abort(ContainersPruneProps, data)

        response = DockerEngine().run_container_operation(
            operation=payload['operation'],
            data=payload['data']
        )
        schema = ContainerObj if response else None
        return parse_data(schema, response) if response \
            else response_by_success(False)
