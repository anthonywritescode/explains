def myrepr(o):
    # return type(o).__repr__(o)
    tp = type(o)
    return tp.__repr__(o)


class C:
    def __repr__(self):
        return 'C repr'


class D(C):
    def __repr__(self):
        return myrepr(super()) + ' + ' + super().__repr__()
