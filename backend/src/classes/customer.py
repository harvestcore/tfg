from config.server_environment import BASE_DATABASE

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
        Check if the given customer name exists
        @param Customer's name
    """
    def is_customer(self, customer):
        MongoEngine().set_collection_name(BASE_DATABASE)
        if customer == '' or customer == 'localhost':
            return True
        elif customer != BASE_DATABASE:
            c = self.find({'domain': customer})
            if c.data is not None and c.data['enabled']:
                return True
        return False

    """
        Set the current customer
        @param Customer's name
    """
    def set_customer(self, customer):
        if customer != BASE_DATABASE:
            c = self.find({'domain': customer})
            if c.data is not None:
                return MongoEngine().set_collection_name(c.data['db_name'])
        else:
            MongoEngine().set_collection_name(BASE_DATABASE)

    def insert(self, item=None):
        if item is None or not item or \
                'domain' not in item or 'db_name' not in item:
            return False

        self.set_customer(BASE_DATABASE)

        if MongoEngine().get_client() is not None:
            found = self.find(
                criteria={
                    'domain': item['domain'],
                    'db_name': item['db_name']
                },
                projection={'domain': 1, 'db_name': 1}
            ).data

            if found is not None:
                return False

        insertion = super().insert(data=item)

        return insertion

    def find(self, criteria={}, projection={}):
        self.set_customer(BASE_DATABASE)
        return super().find(criteria, projection)

    def update(self, criteria, data):
        self.set_customer(BASE_DATABASE)
        return super().update(criteria, data)

    def remove(self, criteria={}, force=False):
        self.set_customer(BASE_DATABASE)
        return super().remove(criteria, force)
