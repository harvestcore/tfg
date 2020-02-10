from flask import Blueprint
from src.classes.blueprint import bp
from src.classes.customer import Customer


test = Blueprint(name='test', url_prefix='/test', import_name='test')


@bp(blueprint=test, class_name=Customer.__name__, path='/', methods=['get'])
class Testt:
    @staticmethod
    def get(a):
        return {'get': 'get', 'a': a}

    @staticmethod
    def post(a):
        return {'post': 'post', 'a': a}


@test.route(rule='/', methods=['GET'])
def fff():
    return {'hello': 'world'}
