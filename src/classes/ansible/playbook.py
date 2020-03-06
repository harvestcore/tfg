import yaml

from src.classes.item import Item


class Playbook(Item):
    table_name = 'playbooks'
    table_schema = {
        'name': 1,
        'playbook': 1,
        'creation_time': 1,
        'last_modified': 1,
        'enabled': 1,
        'deleted': 1,
        'delete_time': 1
    }

    def __init__(self):
        super(Playbook, self).__init__()

    def insert(self, data=None):
        if data is not None:
            return super().insert(data={
                'name': data['name'],
                'playbook': [yaml.load(data['playbook'])]
            })
        return False
