class C:
    def __init__(self, x):
        self.x = x

    def mutator(self, y):
        self.y = y


class D(C):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z
