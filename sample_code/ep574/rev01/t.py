empty = object()


class Lazy:
    def __init__(self, f):
        self._f = f
        self._inst = empty

    def __getattr__(self, attr):
        if self._inst is empty:
            self._inst = self._f()

        return getattr(self._inst, attr)


class C:
    def __init__(self):
        print('expensive!')

    def foo(self):
        print('foo() was called')


def make_c():
    return C()


lazy = Lazy(make_c)
lazy.foo()
lazy.foo()
