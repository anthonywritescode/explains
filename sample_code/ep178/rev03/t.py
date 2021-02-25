

class _PrivateClass:
    ...


class PublicClass:
    pass


def _private_api():
    ...


def public_api():
    _private_api()


class C:
    def __init__(self):
        breakpoint()

    def __repr__(self): return 'repr of C()'

    def __magic_api__(self): ...

    def __mangled_api(self): ...

    def _private_api(self): ...

    def public_api(self): ...


print(repr(C()))
