from config.server_environment import BASE_COLLECTION

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
        MongoEngine().set_collection_name(BASE_COLLECTION)
        if customer != BASE_COLLECTION:
            c = self.find({'domain': customer})
            if c.data is not None:
                return True
        elif customer == '':
            return True
        return False

    """
        Set the current customer
        @param Customer's name
    """
    def set_customer(self, customer):
        MongoEngine().set_collection_name(BASE_COLLECTION)
        if customer != BASE_COLLECTION:
            c = self.find({'domain': customer})
            if c.data is not None:
                return MongoEngine().set_collection_name(c.data['db_name'])

    def insert(self, item=None):
        if item is None:
            return False

        self.set_customer(BASE_COLLECTION)

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
