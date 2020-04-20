import json
import unittest

from src.app import app
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine

from tests.utils.login import TestingLogin

from config.server_environment import TESTING_DATABASE


class UserServiceTests(unittest.TestCase):
    app = app.test_client()
    headers = TestingLogin().headers
    path = '/api/customer'

    def setUp(self):
        Customer().set_customer(TESTING_DATABASE)

    def test_create_customer(self):
        customer = {
            'domain': 'test-customer',
            'db_name': 'test-customer'
        }
        response = self.app.post(
            self.path,
            headers=self.headers,
            data=json.dumps(customer)
        )
        self.assertEqual(response.status_code, 200, 'Customer not created')

        response = self.app.delete(
            self.path,
            headers=self.headers,
            data=json.dumps({'domain': 'test-customer'})
        )
        self.assertEqual(response.status_code, 204, 'User not deleted')

    def test_update_customer(self):
        customer = {
            'domain': 'test-customer2',
            'db_name': 'test-customer2'
        }
        response = self.app.post(
            self.path,
            headers=self.headers,
            data=json.dumps(customer)
        )
        self.assertEqual(response.status_code, 200, 'Customer not created')

        customer = {
            'domain': 'test-c2',
            'db_name': 'test-c2',
            'enabled': True
        }
        response = self.app.put(
            self.path,
            headers=self.headers,
            data=json.dumps({'domain': 'test-customer2', 'data': customer})
        )
        self.assertEqual(response.status_code, 200, 'Customer not updated')

        response = self.app.delete(
            self.path,
            headers=self.headers,
            data=json.dumps({'domain': 'test-customer2'})
        )
        self.assertEqual(response.status_code, 204, 'Customer not deleted')

    def test_delete_non_existent_customer(self):
        response = self.app.delete(
            self.path,
            headers=self.headers,
            data=json.dumps({'domain': 'non-existing-domain'})
        )
        self.assertEqual(response.status_code, 204, 'Customer not deleted')

    def test_query_users(self):
        c1 = {
            'domain': 'test-customer3',
            'db_name': 'test-customer3'
        }

        c2 = {
            'domain': 'test-customer4',
            'db_name': 'test-customer4'
        }

        response = self.app.post(
            self.path,
            headers=self.headers,
            data=json.dumps(c1)
        )
        self.assertEqual(response.status_code, 200, 'C1 not created')

        response = self.app.post(
            self.path,
            headers=self.headers,
            data=json.dumps(c2)
        )
        self.assertEqual(response.status_code, 200, 'C2 not created')

        response = self.app.post(
            self.path + '/query',
            headers=self.headers,
            data=json.dumps({
                'query': {
                    'enabled': True
                }
            })
        )
        self.assertEqual(response.status_code, 200, 'Customers not found')
        self.assertGreaterEqual(json.loads(response.data)['total'], 2)

        response = self.app.post(
            self.path + '/query',
            headers=self.headers,
            data=json.dumps({
                'query': {},
                'filter': {
                    'domain': 1
                }
            })
        )
        self.assertEqual(response.status_code, 200, 'Customers not found')
        self.assertGreaterEqual(json.loads(response.data)['total'], 2)
        for user in json.loads(response.data)['items']:
            self.assertEqual(list(user.keys()), ['domain'], 'Wrong keys')

        response = self.app.delete(
            self.path,
            headers=self.headers,
            data=json.dumps(c1)
        )
        self.assertEqual(response.status_code, 204, 'C1 not deleted')

        response = self.app.delete(
            self.path,
            headers=self.headers,
            data=json.dumps(c2)
        )
        self.assertEqual(response.status_code, 204, 'C2 not deleted')
