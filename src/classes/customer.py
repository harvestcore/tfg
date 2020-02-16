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
        Set the current customer
        @param Customer's name
    """
    @classmethod
    def set_customer(cls, customer):
        MongoEngine().set_collection_name(customer)

    def insert(self, item=None):
        if item is None:
            return False
        elif MongoEngine().get_client() is not None:
            if item['domain'] in super().find(
                    criteria={'domain': item['domain']}).data:
                return False

        self.set_customer(BASE_COLLECTION)
        insertion = super().insert(data=item)
        if insertion:
            self.set_customer(customer=item['db_name'])

        return insertion

