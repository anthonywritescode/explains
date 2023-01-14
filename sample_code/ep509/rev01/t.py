class C:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, attr):
        print(f'unrecognized attribute: {attr}')
        return f'got {attr}'


c = C(1)
print(c.x)
print(c.unknown_attribute_here)
