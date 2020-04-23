import json
import uuid
from datetime import datetime
from bson.json_util import dumps
from cryptography.fernet import Fernet

from src.classes.mongo_engine import MongoEngine
from src.classes.operation import Operation
from src.utils.time import convert_to_string

from config.server_environment import ENC_KEY


class Item:
    table_name = ''
    table_schema = {}
    data = {}

    def __init__(self):
        pass

    """
        Return the cursor to the table
    """
    def cursor(self):
        if self.table_name != '':
            return MongoEngine().get_client()[self.table_name]
        return None

    """
        Find all the elements by the given criteria
    """
    def find(self, criteria={}, projection={}):
        _projection = projection if projection else self.table_schema
        data = json.loads(
            dumps(self.cursor().find(criteria, _projection)))
        data_length = len(data)
        if data_length == 0:
            self.data = None
        elif data_length == 1:
            self.data = data[0]
        else:
            self.data = data

        return self

    """
        Insert an item
    """
    def insert(self, data=None):
        info = {
            'enabled': True,
            'deleted': False,
            'creation_time': convert_to_string(datetime.now()),
            'last_modified': convert_to_string(datetime.now()),
            'delete_time': 0
        }

        if data is None:
            return False
        elif type(data) is dict:
            _operation = Operation.INSERT.value + Operation.ONE.value
            data.update(info)
            if 'password' in data.keys():
                password = Fernet(ENC_KEY).encrypt(data['password'].encode())\
                    .decode('utf-8')
                data.update({'password': password})

            if 'public_id' in self.table_schema.keys()\
                    and 'public_id' not in data.keys():
                data.update({'public_id': str(uuid.uuid4())})
        elif type(data) is list:
            _operation = Operation.INSERT.value + Operation.MANY.value
            for item in data:
                item.update(info)
        else:
            return False

        try:
            getattr(self.cursor(), _operation)(data)
            return True
        except Exception:
            return False

    """
        'Remove' an item by the given criteria. It doesn't removes the item,
        only marks it as deleted
    """
    def remove(self, criteria={}, force=False):
        info = {
            'enabled': False,
            'deleted': True,
            'delete_time': convert_to_string(datetime.now())
        }

        if not force:
            return self.update(criteria=criteria, data=info)

        try:
            self.cursor().delete_one(filter=criteria)
            return True
        except Exception:
            return False

    """
        Update the item that fits the criteria with the new data
    """
    def update(self, criteria, data):
        try:
            self.cursor().update_one(filter=criteria, update={'$set': data})
            return True
        except Exception:
            return False
