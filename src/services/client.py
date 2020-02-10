from flask import Blueprint

# GET, POST, DELETE
client_bp = Blueprint(name='client', url_prefix='/client', import_name='client')


@client_bp.route(rule='/', methods=['GET'])
def get():
    return {'a': 'test'}
