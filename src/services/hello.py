from flask import Blueprint
from src.classes.blueprint import bp
from src.classes.customer import Customer


test = Blueprint(name='test', url_prefix='/test', import_name='test')


@bp(blueprint=test, bp_class=Customer, path='/', methods=['get', 'post'])
class Testt:
    @staticmethod
    def get():
        return {'get': 'get', 'a': 1}

    @staticmethod
    def post():
        return {'post': 'post', 'a': 1}

    @staticmethod
    def put():
        return {'put': 'put', 'a': 1}

    @staticmethod
    def delete():
        return {'delete': 'delete', 'a': 1}


@test.route(rule='/', methods=['GET'])
def fff():
    return {'hello': 'world'}
