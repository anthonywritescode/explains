class User(tuple):
    _fields = ('name', 'age', 'location')

    def __new__(cls, name, age, location):
        return tuple.__new__(cls, (name, age, location))

    @property
    def name(self):
        return self[0]

    @property
    def age(self):
        return self[1]

    @property
    def location(self):
        return self[2]

    def __repr__(self):
        return (
            f'{type(self).__name__}('
            f'name={self.name!r}, age={self.age!r}, location={self.location!r}'
            ')'
        )

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
