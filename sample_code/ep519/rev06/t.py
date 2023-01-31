# 1. data-descriptors
# 2. self.__dict__['d']
# 3. non-data-descrptors


class D:
    def __init__(self):
        print('__init__')

    def __set_name__(self, owner, name):
        print('__set_name__')
        self.d_name = name

    def __set__(self, inst, val):
        print(f'got __set__ with {val}')
        setattr(inst, f'_{self.d_name}', val)

    def __delete__(self, inst):
        delattr(inst, f'_{self.d_name}')

    # C.d
    # inst=<class C>, owner=None
    # c.d
    # inst=<C object>, owner=<class C>

    def __get__(self, inst, owner=None):
        if owner is None:
            return self

        print('__get__')
        return getattr(inst, f'_{self.d_name}', 5)


class C:
    d = D()

    @property
    def f(self):
        return 9001

    def __init__(self):
        self.__dict__['d'] = 9


class cached_property:
    def __init__(self, fn):
        self.fn = fn
        self.name = fn.__name__

    def __set_name(self, owner, name):
        self.name = name

    def __get__(self, inst, owner=None):
        if owner is None:
            return self

        ret = inst.__dict__[self.name] = self.fn(inst)
        # ret = inst.__dict__[self.name] = self.fn.__get__(inst, owner)()
        return ret


class Q:
    @cached_property
    def f(self):
        print('computing f')
        return 9001
