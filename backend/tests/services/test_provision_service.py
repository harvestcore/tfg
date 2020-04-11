import requests
from flask_testing import LiveServerTestCase

from src.app import app
from src.classes.user import User
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine
from src.classes.docker_engine import DockerEngine
from src.classes.ansible.host import Host
from src.classes.ansible.playbook import Playbook

from config.server_environment import TESTING_COLLECTION


class ProvisionHostServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        self.path = '/api/provision/hosts'

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

    def test_create_host(self):
        host = {
            'name': 'benjamin',
            'ips': ['10.10.10.10']
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=host
        )
        self.assertEqual(response.status_code, 200, 'Host not created')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'benjamin'}
        )
        self.assertEqual(response.status_code, 204, 'Host not deleted')

    def test_update_host(self):
        host = {
            'name': 'harry',
            'ips': ['10.10.10.10']
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=host
        )
        self.assertEqual(response.status_code, 200, 'Host not created')

        host = {
            'name': 'harry',
            'ips': ['10.10.10.10', '20.20.20.20']
        }
        response = requests.put(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'harry', 'data': host}
        )
        self.assertEqual(response.status_code, 200, 'Host not updated')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'harry'}
        )
        self.assertEqual(response.status_code, 204, 'Host not deleted')

    def test_delete_non_existent_host(self):
        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'fernando'}
        )
        self.assertEqual(response.status_code, 204, 'Host not deleted')

    def test_get_host_by_name(self):
        host = {
            'name': 'lucas',
            'ips': ['10.10.10.10']
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=host
        )
        self.assertEqual(response.status_code, 200, 'Host not created')

        response = requests.get(
            self.get_server_url() + self.path + '/' + host['name'],
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200, 'Host not fetched')
        self.assertEqual(response.json()['name'], host['name'], 'Wrong name')
        self.assertEqual(response.json()['ips'], host['ips'], 'Wrong ips')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'lucas'}
        )
        self.assertEqual(response.status_code, 204, 'Host not deleted')

    def test_query_hosts(self):
        host1 = {
            'name': 'margarita',
            'ips': ['10.10.10.10']
        }

        host2 = {
            'name': 'vera',
            'ips': ['10.10.10.10']
        }

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=host1
        )
        self.assertEqual(response.status_code, 200, 'Host1 not created')

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=host2
        )
        self.assertEqual(response.status_code, 200, 'Host2 not created')

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {}
            }
        )
        self.assertEqual(response.status_code, 200, 'Hosts not found')
        self.assertGreaterEqual(response.json()['total'], 2, 'Too many hosts')

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {},
                'filter': {
                    'ips': 1
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Hosts not found')
        self.assertGreaterEqual(response.json()['total'], 2, 'Too many hosts')
        for user in response.json()['items']:
            self.assertEqual(list(user.keys()), ['ips'], 'Wrong keys')


class ProvisionPlaybookServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8082
        self.path = '/api/provision/playbook'

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

    def test_create_playbook(self):
        playbook = {
            'name': 'arthur',
            'playbook': {
                'hosts': 'arthur',
                'remote_user': 'arthur',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=playbook
        )
        self.assertEqual(response.status_code, 200, 'Playbook not created')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'arthur'}
        )
        self.assertEqual(response.status_code, 204, 'Playbook not deleted')

    def test_update_playbook(self):
        playbook = {
            'name': 'arthur',
            'playbook': {
                'hosts': 'arthur',
                'remote_user': 'arthur',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=playbook
        )
        self.assertEqual(response.status_code, 200, 'Playbook not created')

        playbook = {
            'name': 'arthur',
            'playbook': {
                'hosts': 'modified_arthur',
                'remote_user': 'modified_arthur',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }
        response = requests.put(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'arthur', 'data': playbook}
        )
        self.assertEqual(response.status_code, 200, 'Playbook not updated')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'arthur'}
        )
        self.assertEqual(response.status_code, 204, 'Playbook not deleted')

    def test_delete_non_existent_playbook(self):
        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'frank'}
        )
        self.assertEqual(response.status_code, 204, 'Playbook not deleted')

    def test_get_playbook_by_name(self):
        playbook = {
            'name': 'lewis',
            'playbook': {
                'hosts': 'lewis',
                'remote_user': 'lewis',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=playbook
        )
        self.assertEqual(response.status_code, 200, 'Playbook not created')

        response = requests.get(
            self.get_server_url() + self.path + '/' + playbook['name'],
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200, 'Playbook not fetched')
        self.assertEqual(response.json()['name'], playbook['name'],
                         'Wrong name')
        self.assertEqual(response.json()['playbook'][0], playbook['playbook'],
                         'Wrong playbook')

        response = requests.delete(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={'name': 'lewis'}
        )
        self.assertEqual(response.status_code, 204, 'Playbook not deleted')

    def test_query_playbooks(self):
        playbook1 = {
            'name': 'agnes',
            'playbook': {
                'hosts': 'agnes',
                'remote_user': 'agnes',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }

        playbook2 = {
            'name': 'betty',
            'playbook': {
                'hosts': 'betty',
                'remote_user': 'betty',
                'tasks': [
                    {
                        'name': 'test debug',
                        'debug': {
                            'msg': 'Debug msg'
                        }
                    }
                ]
            }
        }

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=playbook1
        )
        self.assertEqual(response.status_code, 200, 'Playbook1 not created')

        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json=playbook2
        )
        self.assertEqual(response.status_code, 200, 'Playbook2 not created')

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {}
            }
        )
        self.assertEqual(response.status_code, 200, 'Playbooks not found')
        self.assertGreaterEqual(response.json()['total'], 2)

        response = requests.post(
            self.get_server_url() + self.path + '/query',
            headers=self.headers,
            json={
                'query': {},
                'filter': {
                    'playbook': 1
                }
            }
        )
        self.assertEqual(response.status_code, 200, 'Playbooks not found')
        self.assertGreaterEqual(response.json()['total'], 2)
        for user in response.json()['items']:
            self.assertEqual(list(user.keys()), ['playbook'], 'Wrong keys')


class ProvisionRunPlaybooksServiceTests(LiveServerTestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8083
        self.path = '/api/provision'
        self.ips = ['172.17.0.2']
        self.playbook = 'test-alpine-ssh'
        self.hosts = ['alpine']

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

    def test_run_playbook(self):
        h = Host().insert({
            'name': self.hosts[0],
            'ips': self.ips
        })

        self.assertEqual(h, True, 'Host not added')

        p = Playbook().insert({
            'name': self.playbook,
            'playbook': {
                'hosts': self.hosts[0],
                'remote_user': 'root',
                'tasks': [
                    {
                        'name': 'Test debug msg',
                        'debug': {
                            'msg': 'This works!'
                        }
                    }
                ]
            }
        })

        self.assertEqual(p, True, 'Playbook not added')

        container = DockerEngine().run_container_operation(
            operation='run',
            data={
                'image': 'sickp/alpine-sshd',
                'detach': True
            }
        )

        self.assertNotEqual(container, False, 'Cointainer not running')
        self.container_id = container.short_id

        # Run the playbook
        response = requests.post(
            self.get_server_url() + self.path,
            headers=self.headers,
            json={
                'hosts': self.hosts,
                'playbook': self.playbook,
                'passwords': {
                    'conn_pass': 'root',
                    'become_pass': 'root'
                }
            }
        )

        self.assertEqual(response.status_code, 200, 'Playbook failed running')
        self.assertNotEqual(response.json()['result']
                            .find('PLAY [alpine]'), -1)
        self.assertNotEqual(response.json()['result'].find('[172.17.0.2]'), -1)

        # Stop the container
        c = DockerEngine().get_container_by_id(self.container_id)
        DockerEngine().run_operation_in_object(
            object=c,
            operation='stop',
            data={}
        )
