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
        if self.table_name is not '':
            return MongoEngine().get_client()[self.table_name]
        return None

    """
        Find all the elements by the given criteria
    """
    def find(self, operation=Operation.FIND, criteria={}, projection={}):
        _projection = projection if projection else self.table_schema
        _operation = operation.value if operation is Operation.FIND else Operation.FIND + operation.value
        self.data = getattr(self.cursor(), _operation)(criteria, _projection)
        return self.data

    """
        Insert an item
    """
    def insert(self, data=None):
        if data is None:
            return False
        elif type(data) is dict:
            _operation = Operation.INSERT + Operation.ONE
        elif type(data) is list:
            _operation = Operation.INSERT + Operation.MANY
        else:
            return False

        try:
            getattr(self.cursor(), _operation)(data)
            return True
        except:
            return False

    """
        Remove an item by the given criteria
    """
    def remove(self, criteria=None):
        if criteria is None:
            criteria = {}
        try:
            self.cursor().delete_one(criteria)
            return True
        except:
            return False

    """
        Update the data of the given item
    """
    def update(self, item, data=None):
        if data is None:
            data = item
        try:
            self.cursor().update_one(item, data)
            return True
        except:
            return False
