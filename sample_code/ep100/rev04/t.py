import collections


class User(collections.namedtuple('User', ('name', 'age', 'location'))):
    __slots__ = ()

    def print_me(self):
        print(f'{self.name} is {self.age} years old and from {self.location}')


def get_users():
    return [
        User('Anthony', 29, 'CA'),
        User('Jeff', 18, 'NY'),
        User('Jason', 16, 'GB'),
    ]


for user in get_users():
    user.print_me()
