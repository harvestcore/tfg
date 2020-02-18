import unittest
from src.classes.customer import Customer
from src.classes.mongo_engine import MongoEngine
from config.server_environment import BASE_COLLECTION


class CustomerTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CustomerTests, self).__init__(*args, **kwargs)

        # Drop previous database
        MongoEngine().drop(BASE_COLLECTION)

    def test_create_customer(self):
        status = Customer().insert({'domain': 'test', 'db_name': 'test'})
        self.assertEqual(status, True)

    def test_create_duplicated_customer(self):
        Customer().insert({'domain': 'test', 'db_name': 'test'})
        status = Customer().insert({'domain': 'test', 'db_name': 'test'})
        self.assertEqual(status, False)
