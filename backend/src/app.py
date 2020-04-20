from flask import Flask, request, abort
from flask_restplus import Api

from src.services.deploy import api as deploy
from src.services.provision import api as provision
from src.services.user import api as user
from src.services.login import api_login as login
from src.services.login import api_logout as logout

from src.classes.customer import Customer

from config.server_environment import DOCKER_ENABLED

app = Flask(__name__)

api = Api(app,
          prefix='/api',
          title='IPManager',
          description='Manage your deploys')
api.add_namespace(provision)
api.add_namespace(user)
api.add_namespace(login)
api.add_namespace(logout)

if DOCKER_ENABLED:
    api.add_namespace(deploy)


@app.before_request
def before_request():
    subdomain = request.host.rsplit('.')[0].rsplit(':')[0]
    if Customer().is_customer(subdomain):
        Customer().set_customer(subdomain)
    else:
        abort(404, "Not found")
