from src.classes.item import Item


class Deploy(Item):
    table_name = 'deploy'
    table_schema = {
    }

    def __init__(self):
        super(Deploy, self).__init__()