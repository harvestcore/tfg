import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from config.server_environment import TESTING_COLLECTION


class UserServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8080
        self.path = '/api/user'

        return app

    def setUp(self):
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
        response = requests.get(self.get_server_url() + '/api/login',
                                auth=('admin', 'admin'))
        self.headers = {'x-access-token': response.json()['token']}

    def test_create_user(self):
        user = {
            'type': 'admin',
            'first_name': 'william',
            'last_name': 'william',
            'username': 'william',
            'email': 'william@domain.com',
            'password': 'william'
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=user
        )
        self.assertEqual(response.status_code, 200, 'User not created')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'email': 'william@domain.com'}
        )
        self.assertEqual(response.status_code, 204, 'User not deleted')

    def test_update_user(self):
        user = {
            'type': 'admin',
            'first_name': 'andrew',
            'last_name': 'andrew',
            'username': 'andrew',
            'email': 'andrew@domain.com',
            'password': 'andrew'
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=user
        )
        self.assertEqual(response.status_code, 200, 'User not created')

        user = {
            'type': 'admin',
            'first_name': 'modified_andrew',
            'last_name': 'modified_andrew',
            'username': 'andrew',
            'email': 'andrew@domain.com',
            'password': 'andrew'
        }
        response = requests.put(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'email': 'andrew@domain.com', 'data': user}
        )
        self.assertEqual(response.status_code, 200, 'User not updated')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'email': 'andrew@domain.com'}
        )
        self.assertEqual(response.status_code, 204, 'User not deleted')

    def test_delete_non_existent_user(self):
        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'email': 'ray@domain.com'}
        )
        self.assertEqual(response.status_code, 204, 'User not deleted')

    def test_get_user_by_name(self):
        user = {
            'type': 'admin',
            'first_name': 'sam',
            'last_name': 'sam',
            'username': 'sam',
            'email': 'sam@domain.com',
            'password': 'sam'
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=user
        )
        self.assertEqual(response.status_code, 200, 'User not created')

        response = requests.get(
            self.get_server_url() + self.path + '/' + user['username'],
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200, 'User not fetched')
        self.assertEqual(response.json()['username'], user['username'],
                         'Wrong username')
        self.assertEqual(response.json()['email'], user['email'],
                         'Wrong email')
        self.assertIsInstance(response.json()['public_id'], str,
                              'Wrong public_id')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'email': 'sam@domain.com'}
        )
        self.assertEqual(response.status_code, 204, 'User not deleted')

    def test_query_users(self):
        user1 = {
            'type': 'admin',
            'first_name': 'violet',
            'last_name': 'violet',
            'username': 'violet',
            'email': 'violet@domain.com',
            'password': 'violet'
        }

        user2 = {
            'type': 'admin',
            'first_name': 'julia',
            'last_name': 'julia',
            'username': 'julia',
            'email': 'julia@domain.com',
            'password': 'julia'
        }

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=user1
        )
        self.assertEqual(response.status_code, 200, 'User1 not created')

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=user2
        )
        self.assertEqual(response.status_code, 200, 'User2 not created')

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {
                    'type': 'admin'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Users not found')
        self.assertGreaterEqual(response.json()['total'], 2)

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {},
                'filter': {
                    'username': 1
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Users not found')
        self.assertGreaterEqual(response.json()['total'], 2)
        for user in response.json()['items']:
            self.assertEqual(list(user.keys()), ['username'], 'Wrong keys')
