import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from config.server_environment import TESTING_COLLECTION


class DeployImageServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        self.path = '/api/deploy'

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

    def test_pull_and_remove_image(self):
        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'pull',
                'data': {
                    'repository': 'alpine:latest'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not pulled')

        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'remove',
                'data': {
                    'image': 'alpine',
                    'force': True
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not removed')

    def test_get_image(self):
        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'pull',
                'data': {
                    'repository': 'alpine:latest'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not pulled')
        short_id = response.json()['short_id']

        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'get',
                'data': {
                    'name': 'alpine'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not fetched')
        self.assertEqual(response.json()['short_id'], short_id,
                         'Image not fetched')

        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'remove',
                'data': {
                    'image': 'alpine',
                    'force': True
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not removed')

    def test_prune_images(self):
        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'prune',
                'data': {
                    'filters': {
                        'dangling': True
                    }
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Images not pruned')
        self.assertEqual(response.json(), {}, 'Images not pruned')

    def test_search_image(self):
        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'search',
                'data': {
                    'term': 'alpine'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Images not searched')
        self.assertGreaterEqual(response.json()['total'],  0,
                                'Images not searched')

    def test_history_image(self):
        response = requests.post(
            self.get_server_url() + self.path + '/image',
            headers=self.headers,
            json={
                'operation': 'pull',
                'data': {
                    'repository': 'alpine:latest'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image not pulled')

        response = requests.post(
            self.get_server_url() + self.path + '/image/single',
            headers=self.headers,
            json={
                'name': 'alpine',
                'operation': 'history',
                'data': {}
            }
        )
        self.assertEqual(response.status_code, 200, 'No history fetched')
        self.assertEqual(response.json(), {}, 'History available')
