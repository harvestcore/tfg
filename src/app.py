from flask import Flask
from flask_restplus import Api
from flask_marshmallow import Marshmallow

from src.services.client import api as client
from src.services.deploy import api as deploy
from src.services.deploy_config import api as deploy_config
from src.services.provision import api as provision
from src.services.provision_config import api as provision_config
from src.services.user import api as user

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

if __name__ == '__main__':
    app.run(debug=True)
