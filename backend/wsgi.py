from flask import Flask, request, abort
from flask_restplus import Api

from src.services.client import api as client
from src.services.deploy import api as deploy
from src.services.deploy_config import api as deploy_config
from src.services.provision import api as provision
from src.services.provision_config import api as provision_config
from src.services.user import api as user
from src.services.login import api as login

from src.classes.customer import Customer

app = Flask(__name__)

api = Api(app,
          prefix='/api',
          title='IPManager',
          description='Manage your deploys')
api.add_namespace(client)
api.add_namespace(deploy)
api.add_namespace(deploy_config)
api.add_namespace(provision)
api.add_namespace(provision_config)
api.add_namespace(user)
api.add_namespace(login)


@app.before_request
def before_request():
    subdomain = request.host[:-len('localhost:5000')].rstrip('.')
    if Customer().is_customer(subdomain):
        Customer().set_customer(subdomain)
    else:
        abort(404, "Not found")


if __name__ == "__main__":
    app.run()
