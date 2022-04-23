class C:
    def __repr__(self):
        return 'C repr'


class D(C):
    def __repr__(self):
        return super().__repr__()
