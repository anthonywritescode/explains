import contextlib


class mcs(type):
    def __subclasscheck__(self, tp):
        return True


class Weird(Exception, metaclass=mcs):
    pass


with contextlib.suppress(Weird):
    raise ValueError

try:
    raise ValueError
except Weird:
    pass
