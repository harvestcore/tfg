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
        self.assertEqual(status, True, "Customer not added")

    def test_create_duplicated_customer(self):
        Customer().insert({'domain': 'test', 'db_name': 'test'})
        status = Customer().insert({'domain': 'test', 'db_name': 'test'})
        self.assertEqual(status, False, "Added duplicated customer")

    def test_find_all_customers(self):
        c1 = {'domain': 'test', 'db_name': 'test'}
        c2 = {'domain': 'test2', 'db_name': 'test2'}
        Customer().insert(c1)
        Customer().insert(c2)
        Customer().set_customer(BASE_COLLECTION)
        customers = Customer().find()

        self.assertNotEqual(customers, None, "Customer obj not created")
        self.assertIsInstance(customers.data, list,
                              "Customer data is not a list")

    def test_find_customer(self):
        c = {'domain': 'test', 'db_name': 'test'}
        keys = ['_id', 'domain', 'db_name', 'enabled', 'deleted',
                'creation_time', 'last_modified', 'delete_time']
        Customer().insert(c)
        Customer().set_customer(BASE_COLLECTION)
        customer = Customer().find()

        self.assertNotEqual(customer, None, "Customer obj not created")
        self.assertIsInstance(customer.data, dict,
                              "Customer data is not a dict")
        self.assertEqual(customer.data['domain'], c['domain'],
                         "Domain not equal")
        self.assertEqual(customer.data['db_name'], c['db_name'],
                         "Database name not equal")
        self.assertListEqual(list(customer.data.keys()), keys,
                             "Keys are not equal")

    def test_find_customer_by_criteria(self):
        c = {'domain': 'test', 'db_name': 'test'}
        Customer().insert(c)
        Customer().set_customer(BASE_COLLECTION)
        not_found_customer = Customer().find({'domain': 'rip'})

        self.assertEqual(not_found_customer.data, None,
                         "Non existing customer found")

        found_customer = Customer().find({'domain': 'test'})

        self.assertNotEqual(found_customer.data, {},
                            "Existing customer without data")

    def test_find_customer_by_criteria_with_projection(self):
        c = {'domain': 'test', 'db_name': 'test'}
        keys = ['_id', 'enabled']
        Customer().insert(c)
        Customer().set_customer(BASE_COLLECTION)

        found_customer = Customer().find(criteria={'domain': 'test'},
                                         projection={'_id': 1, 'enabled': 1})

        self.assertListEqual(list(found_customer.data.keys()), keys,
                             "Wrong keys while finding with projection")

    def test_remove_customer(self):
        c = {'domain': 'test', 'db_name': 'test'}
        Customer().insert(c)
        Customer().set_customer(BASE_COLLECTION)

        customer = Customer().find()
        Customer().remove(c)
        deleted_customer = Customer().find()

        self.assertEqual(customer.data['creation_time'],
                         deleted_customer.data['creation_time'],
                         "Deleted item with weird creation time")
        self.assertNotEqual(customer.data['enabled'],
                            deleted_customer.data['enabled'],
                            "Deleted item enabled")
        self.assertNotEqual(customer.data['deleted'],
                            deleted_customer.data['deleted'],
                            "Deleted item not deleted")
