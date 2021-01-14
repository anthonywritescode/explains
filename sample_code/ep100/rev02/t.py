import collections


User = collections.namedtuple('User', ('name', 'age', 'location'))


def get_users():
    return [
        User('Anthony', 29, 'CA'),
        User('Jeff', 18, 'NY'),
        User('Jason', 16, 'GB'),
    ]


for name, age, location in get_users():
    print(f'{name} is {age} years old and from {location}')
