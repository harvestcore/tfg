from PyInquirer import prompt

from src.classes.customer import Customer


def create_customer(c):
    return Customer().insert(c)


def list_customers(enabled):
    data = Customer().find({'enabled': enabled}, projection={'domain': 1}).data
    if type(data) is dict:
        return [{'name': data['domain']}]
    if data is not None:
        return [{'name': item['domain']} for item in data]
    return []


def enable_customer(enabled, name):
    return Customer().update({'domain': name}, data={'enabled': enabled})


operations = [
    {
        'type': 'list',
        'name': 'operation',
        'message': 'What you want to do?',
        'choices': [
            {
                'name': 'Create a customer'
            },
            {
                'name': 'Enable a customer'
            },
            {
                'name': 'Disable a customer'
            },
            {
                'name': 'Exit'
            }
        ]
    }
]

if __name__ == '__main__':
    answer = prompt(operations)['operation']

    if answer == 'Create a customer':
        customer = prompt([
            {
                'type': 'input',
                'name': 'domain',
                'message': 'Enter a customer name',
                'validate': lambda value: value != ''
            },
            {
                'type': 'input',
                'name': 'db_name',
                'message': 'Enter a database name',
                'validate': lambda value: value != ''
            }
        ])

        if create_customer(customer):
            print("Customer created successfully")

    elif answer == 'Enable a customer':
        data = list_customers(enabled=False)
        if len(data) == 0:
            print("There are no customers disabled")
            exit(1)

        customer = prompt({
            'type': 'list',
            'name': 'customer',
            'message': 'Which customer do you want to enable?',
            'choices': data
        })

        if enable_customer(True, customer['customer']):
            print("User enabled successfully")

    elif answer == 'Disable a customer':
        data = list_customers(enabled=True)
        if len(data) == 0:
            print("There are no customers enabled")
            exit(1)

        customer = prompt({
            'type': 'list',
            'name': 'customer',
            'message': 'Which customer do you want to disable?',
            'choices': data
        })

        if enable_customer(False, customer['customer']):
            print("User disabled successfully")

    elif answer == 'Exit':
        exit(0)
