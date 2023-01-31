# 1. data-descriptors
# 2. self.__dict__['d']
# 3. non-data-descrptors


class D:
    def __init__(self):
        print('__init__')

    # __set_name__

    def __set__(self, inst, val):
        print(f'got __set__ with {val}')
        inst.secret_val = val

    def __delete__(self, inst):
        del inst.secret_val

    def __get__(self, inst, owner=None):
        print('__get__')
        return getattr(inst, 'secret_val', 5)


class C:
    d = D()

    def __init__(self):
        self.__dict__['d'] = 9


print(C().d)
