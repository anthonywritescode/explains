class C:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, attr):
        print(f'unrecognized attribute: {attr}')
        return f'got {attr}'


c = C(1)


def __getattr__(attr):
    return f'unknown: {attr}'


def __dir__():
    return list(globals()) + ['foo']
