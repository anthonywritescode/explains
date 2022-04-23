class C:
    def __repr__(self):
        return 'C repr'


class D(C):
    def __repr__(self):
        return repr(super())
