import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from config.server_environment import TESTING_COLLECTION


class DeployContainerServiceTests(LiveServerTestCase):
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

    def test_run_hello_world_container(self):
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

    def test_get_running_container(self):
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
            self.get_server_url() + self.path + '/container',
            headers=self.headers,
            json={
                'operation': 'get',
                'data': {
                    'container_id': short_id
                }
            }
        )

        self.assertEqual(response.status_code, 200,
                         'Container info not fetched')
        self.assertEqual(response.json()['short_id'], short_id,
                         'Wrong container')

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

    def test_list_running_containers(self):
        response1 = requests.post(
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
        self.assertEqual(response1.status_code, 200, 'Container not run')
        self.assertEqual(response1.json()['status'], 'created',
                         'Container not created')

        response2 = requests.post(
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
        self.assertEqual(response2.status_code, 200, 'Container not run')
        self.assertEqual(response2.json()['status'], 'created',
                         'Container not created')

        short_id_1 = response1.json()['short_id']
        short_id_2 = response2.json()['short_id']

        response = requests.post(
            self.get_server_url() + self.path + '/container',
            headers=self.headers,
            json={
                'operation': 'list',
                'data': {
                    'all': False
                }
            }
        )

        self.assertEqual(response.status_code, 200,
                         'Container list not fetched')
        self.assertGreaterEqual(response.json()['total'], 2,
                                'Wrong container number')

        response1 = requests.post(
            self.get_server_url() + self.path + '/container/single',
            headers=self.headers,
            json={
                'container_id': short_id_1,
                'operation': 'stop',
                'data': {}
            }
        )

        response2 = requests.post(
            self.get_server_url() + self.path + '/container/single',
            headers=self.headers,
            json={
                'container_id': short_id_2,
                'operation': 'stop',
                'data': {}
            }
        )

        self.assertEqual(response1.status_code, 200, 'Container1 not stopped')
        self.assertEqual(response2.status_code, 200, 'Container2 not stopped')

    def test_prune_containers(self):
        response = requests.post(
            self.get_server_url() + self.path + '/container',
            headers=self.headers,
            json={
                'operation': 'prune',
                'data': {}
            }
        )
        self.assertEqual(response.status_code, 200, 'Containers not pruned')
        self.assertEqual(response.json(), {}, 'Containers not pruned')

    def test_kill_container(self):
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
                'operation': 'kill',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not killed')
        self.assertEqual(response.json()['data'], None, 'Container not killed')

    def test_logs_container(self):
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
                'operation': 'logs',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not stopped')
        self.assertEqual(response.json()['data'], '', 'Container with logs')

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
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

    def test_pause_unpause_container(self):
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
                'operation': 'pause',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not paused')
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

        response = requests.post(
            self.get_server_url() + self.path + '/container/single',
            headers=self.headers,
            json={
                'container_id': short_id,
                'operation': 'unpause',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not unpaused')
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

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
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

    def test_reload_container(self):
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
                'operation': 'reload',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not reloaded')
        self.assertEqual(response.json()['data'], None,
                         'Container not reloaded')

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
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

    def test_rename_container(self):
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
                'operation': 'rename',
                'data': {
                    'name': 'testing-name'
                }
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not renamed')
        self.assertEqual(response.json()['data'], None,
                         'Container not renamed')

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
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')

    def test_rename_container(self):
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
                'operation': 'restart',
                'data': {}
            }
        )

        self.assertEqual(response.status_code, 200, 'Container not restarted')
        self.assertEqual(response.json()['data'], None,
                         'Container not restarted')

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
        self.assertEqual(response.json()['data'], None,
                         'Container not stopped')
