from flask import Flask
from flask_restplus import Api
from flask_marshmallow import Marshmallow

from config.server_environment import BASE_COLLECTION

from src.services.client import api as client
from src.services.deploy import api as deploy
from src.services.deploy_config import api as deploy_config
from src.services.provision import api as provision
from src.services.provision_config import api as provision_config
from src.services.user import api as user
from src.classes.customer import Customer

app = Flask(__name__)
api = Api(app,
          prefix='/api',
          title='IPManager',
          description='Manage your deploys')

ma = Marshmallow(app)

api.add_namespace(client)
api.add_namespace(deploy)
api.add_namespace(deploy_config)
api.add_namespace(provision)
api.add_namespace(provision_config)
api.add_namespace(user)

Customer().set_customer(BASE_COLLECTION)

if __name__ == '__main__':
    app.run(debug=True)
