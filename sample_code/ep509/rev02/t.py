import sys


class C:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, attr):
        print(f'unrecognized attribute: {attr}')
        return f'got {attr}'


c = C(1)

sys.modules[__name__] = c
