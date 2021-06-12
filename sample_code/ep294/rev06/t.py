class MyStaticMethod:
    def __init__(self, func):
        self._func = func

    def __get__(self, obj, owner=None):
        return self._func


class MyClassMethod:
    def __init__(self, func):
        self._func = func

    def __get__(self, obj, owner=None):
        return self._func.__get__(owner)


class C:
    @MyStaticMethod
    def f():
        print('f was called')

    @MyClassMethod
    def g(cls):
        print(f'g was called from {cls=}')

    def h(self):
        print(f'h was called with {self=}')
