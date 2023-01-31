# 1. data-descriptors
# 2. self.__dict__['d']
# 3. non-data-descrptors


class D:
    def __init__(self):
        print('__init__')

    def __set_name__(self, owner, name):
        self.d_name = name

    def __set__(self, inst, val):
        print(f'got __set__ with {val}')
        setattr(inst, f'_{self.d_name}', val)

    def __delete__(self, inst):
        delattr(inst, f'_{self.d_name}')

    def __get__(self, inst, owner=None):
        print('__get__')
        return getattr(inst, f'_{self.d_name}', 5)


class C:
    d = D()

    def __init__(self):
        self.__dict__['d'] = 9


print(C().d)
