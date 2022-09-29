

def dec(cls):
    class D(cls):
        decorated = True

    return D


@dec
class C:
    hello = 'world'
