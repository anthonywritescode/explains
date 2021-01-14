import collections


User = collections.namedtuple('User', ('name', 'age', 'location'))


def get_users():
    return [
        User('Anthony', 29, 'CA'),
        User('Jeff', 18, 'NY'),
        User('Jason', 16, 'GB'),
    ]


for user in get_users():
    print(f'{user.name} is {user.age} years old and from {user.location}')
