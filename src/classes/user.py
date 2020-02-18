from src.classes.item import Item
from src.classes.operation import Operation


class User(Item):
    table_name = 'users'
    table_schema = {
        'type': 1,
        'first_name': 1,
        'last_name': 1,
        'username': 1,
        'email': 1,
        # 'password': 0,
        'enabled': 1,
        'deleted': 1,
        'creation_time': 1,
        'last_modified': 1,
        'delete_time': 1
    }

    def __init__(self):
        super(User, self).__init__()

    def insert(self, data=None):
        if data is not None:
            current = super(User, self)\
                .find(criteria={'username': data['username'],
                                'email': data['email']})

            if current is []:
                return super(User, self).insert(data)

        return False
