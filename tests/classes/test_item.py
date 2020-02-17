import unittest
from src.classes.customer import Customer
from config.server_environment import BASE_COLLECTION


class ItemTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ItemTests, self).__init__(*args, **kwargs)

        # Setup db
        Customer().set_customer(BASE_COLLECTION)

    # def test_create_customer(self):
    #     status = Customer().insert({'domain': 'test', 'db_name': 'test'})
    #     self.assertEqual(status, True)
    #
    # def test_create_duplicated_customer(self):
    #     status = Customer().insert({'domain': 'test', 'db_name': 'test'})
    #     self.assertEqual(status, False)
