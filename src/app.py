from flask import Flask
from flask_restplus import Api
from flask_marshmallow import Marshmallow

from src.services.hello import test
from src.services.client import client_bp

app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)

app.register_blueprint(test)

app.register_blueprint(client_bp)


if __name__ == '__main__':
    app.run(debug=True)
