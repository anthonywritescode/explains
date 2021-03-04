

def dec(cls):

    class D(cls):
        def foo(self):
            print('hello hello world')

    return D


@dec
class C:
    """hello world"""

    def f(self):
        print('foo')
