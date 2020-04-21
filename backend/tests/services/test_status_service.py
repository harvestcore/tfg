import json
import unittest

from src.app import app
from src.classes.customer import Customer

from tests.utils.login import TestingLogin

from config.server_environment import TESTING_DATABASE


class StatusServiceTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.headers = TestingLogin().headers

    def test_status(self):
        Customer().set_customer(TESTING_DATABASE)

        response = self.app.get(
            '/api/status',
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200, 'Status not found')

        data = json.loads(response.data)
        keys = ['is_up', 'data_usage', 'info']

        self.assertEqual('docker' in data, True, 'Missing docker status')
        self.assertEqual('mongo' in data, True, 'Missing mongo status')

        for key in keys:
            self.assertEqual(key in data['docker'], True,
                             key + ' missing in docker status')
            self.assertEqual(key in data['mongo'], True,
                             key + ' missing in mongo status')
