def make_namedtuple(clsname, fields):
    attrs = {'_fields': fields}

    # make the initialization
    new_method_s = f'''\
def __new__(cls, {", ".join(fields)}):
    return tuple.__new__(cls, ({", ".join(fields)}))
'''
    exec(new_method_s, attrs)
    return type(clsname, (tuple,), attrs)


class User(make_namedtuple('User', ('name', 'age', 'location'))):
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
