import json
from datetime import datetime
from bson.json_util import dumps
from src.classes.mongo_engine import MongoEngine
from src.classes.operation import Operation


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
            self.data = {}
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
            'creation_time': datetime.now(),
            'last_modified': datetime.now(),
            'delete_time': 0
        }

        if data is None:
            return False
        elif type(data) is dict:
            _operation = Operation.INSERT.value + Operation.ONE.value
            data.update(info)
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
        'Remove' an item by the given criteria. It does not removes the item,
        only marks it as deleted
    """
    def remove(self, criteria={}):
        info = {
            'enabled': False,
            'deleted': True,
            'delete_time': datetime.now()
        }

        return self.update(item=criteria, data=info)

    """
        Update the item that fits the criteria with the new data
    """
    def update(self, criteria, data):
        try:
            self.cursor().update_one(filter=criteria, update={'$set': data})
        except Exception:
            return False
