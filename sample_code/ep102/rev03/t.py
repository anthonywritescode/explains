def _make_named_attr_getter(idx: int, name: str):
    def getter(self):
        return self[idx]

    getter.__name__ = name
    return property(getter)


'''
@property
def {name}(self):
    return self[idx]
'''


def _namedtuple_repr(self) -> str:
    fields_s = ', '.join(
        f'{name}={getattr(self, name)!r}'
        for name in self._fields
    )
    return f'{type(self).__name__}({fields_s})'


def make_namedtuple(clsname, fields):
    attrs = {'_fields': fields, '__repr__': _namedtuple_repr}

    # make the initialization
    new_method_s = f'''\
def __new__(cls, {", ".join(fields)}):
    return tuple.__new__(cls, ({", ".join(fields)}))
'''
    exec(new_method_s, attrs)

    for idx, name in enumerate(fields):
        attrs[name] = _make_named_attr_getter(idx, name)

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
