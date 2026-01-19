import warnings
import os.path


_skip_prefixes = (os.path.dirname(__file__),)


def some_func(a=None, b=None):
    if b is not None:
        if a is not None:
            raise TypeError('cannot supply both a= and b=')
        warnings.warn('`b=` is deprecated!', skip_file_prefixes=_skip_prefixes)
        a = b

    print(f'got {a=}')


def some_wrapper(**k):
    print('begin wrapper!')
    some_func(**k)
