import warnings


def some_func(a=None, b=None):
    if b is not None:
        if a is not None:
            raise TypeError('cannot supply both a= and b=')
        warnings.warn('`b=` is deprecated!', stacklevel=2)
        a = b

    print(f'got {a=}')


def some_wrapper(**k):
    print('begin wrapper!')
    some_func(**k)
