# 1. data-descriptors
# 2. self.__dict__['d']
# 3. non-data-descrptors


class D:
    def __init__(self):
        print('__init__')

    # __set_name__
    # __set__
    # __delete__
    def __get__(self, inst, owner=None):
        print('__get__')
        return 5


class C:
    d = D()

    def __init__(self):
        self.__dict__['d'] = 9


print(C().d)
