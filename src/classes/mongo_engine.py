from pymongo import MongoClient
from config.server_environment import MONGO_HOSTNAME, MONGO_PORT


class MongoEngine:
    client = MongoClient(MONGO_HOSTNAME, MONGO_PORT)
    collection = ''
    engine = None

    def __new__(cls, *args, **kwargs):
        if not cls.engine:
            cls.engine = super(MongoEngine, cls).__new__(cls, *args, **kwargs)
        return cls.engine

    """
        Get the customers customers client
    """
    def get_client(self):
        if self.collection is not '':
            return self.client[self.collection]

        return None

    """
        Set the collection name
    """
    def set_collection_name(self, collection):
        self.collection = collection

    """
        Get the current collection name
    """
    def get_collection_name(self):
        return self.collection

    """
        Get all collection names
    """
    def get_collection_names(self):
        return self.get_client().list_database_names()
