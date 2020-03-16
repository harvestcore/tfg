import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from config.server_environment import TESTING_COLLECTION


class LoginServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8080

        Customer().set_customer(TESTING_COLLECTION)
        MongoEngine().drop(TESTING_COLLECTION)
        User().insert({
            'type': 'admin',
            'first_name': 'admin',
            'last_name': 'admin',
            'username': 'admin',
            'email': 'admin@domain.com',
            'password': 'admin'
        })

        return app

    def test_login_and_logout(self):
        response = requests.get(self.get_server_url() + '/api/login',
                                auth=('admin', 'admin'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.json().keys()), ['token'],
                         'There is no token')
        headers = {'x-access-token': response.json()['token']}

        response = requests.get(self.get_server_url() + '/api/logout',
                                headers=headers)
        self.assertEqual(response.status_code, 200, 'Logout failed')
