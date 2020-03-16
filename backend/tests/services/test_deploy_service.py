import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from config.server_environment import TESTING_COLLECTION


class DeployServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8081
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

    def test_run_hello_world_image(self):
        response = requests.post(
            self.get_server_url() + self.path + '/container',
            headers=self.headers,
            json={
                'operation': 'run',
                'data': {
                    'image': 'hello-world'
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Image run failed')

    def test_run_and_stop_background_container(self):
        response = requests.post(
            self.get_server_url() + self.path + '/container',
            headers=self.headers,
            json={
                'operation': 'run',
                'data': {
                    'image': 'mongo:4.2.3',
                    'detach': True
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Container not run')
        self.assertEqual(response.json()['status'], 'created',
                         'Container not created')

        short_id = response.json()['short_id']

        response = requests.post(
            self.get_server_url() + self.path + '/container/single',
            headers=self.headers,
            json={
                'container_id': short_id,
                'operation': 'stop',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not stopped')

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
