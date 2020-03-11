from src.classes.item import Item


class Host(Item):
    table_name = 'hosts'
    table_schema = {
        'name': 1,
        'ips': 1,
        'creation_time': 1,
        'last_modified': 1,
        'enabled': 1,
        'deleted': 1,
        'delete_time': 1
    }

    def __init__(self):
        super(Host, self).__init__()

    def insert(self, data=None):
        if data is not None:
            current = super(Host, self) \
                .find(criteria={'name': data['name']})

            if not current.data:
                return super(Host, self).insert(data)

        return False
