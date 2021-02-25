

class _PrivateClass:
    ...


class PublicClass:
    pass


def _private_api():
    ...


def public_api():
    _private_api()
