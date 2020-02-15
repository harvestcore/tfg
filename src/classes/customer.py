from datetime import datetime

from config.server_environment import DEFAULT_CUSTOMER

from src.classes.mongo_engine import MongoEngine
from src.classes.item import Item


class Customer(Item):
    table_name = 'customers'
    table_schema = {
        'domain': 1,
        'db_name': 1,
        'creation_time': 1,
        'last_modified': 1,
        'enabled': 1,
        'deleted': 1,
        'delete_time': 1
    }

    def __init__(self):
        super(Customer, self).__init__()

    """
        Set the current customer
        @param Customer's name
    """
    @classmethod
    def set_customer(cls, customer):
        MongoEngine().set_collection_name(customer)

    def insert(self, item=None):
        if item is None:
            item = DEFAULT_CUSTOMER
            item['creation_time'] = datetime.now()
        # Item exists (find all items with '_id' == item['_id']
        elif item['_id'] in super().find(criteria={'_id': item['_id']}):
            return False

        return super().insert(data=item)

    @staticmethod
    def get():
        return {'get': '#####', 'a': 1}

    @staticmethod
    def post():
        return {'post': '#####', 'a': 1}

    @staticmethod
    def put():
        return {'put': '#####', 'a': 1}

    @staticmethod
    def delete():
        return {'delete': '#####', 'a': 1}
