import functools


def dec(func):
    @functools.wraps(func)
    def dec_decorator(*args, **kwargs):
        print('inside decorator!')
        return func(*args, **kwargs)
    return dec_decorator


decorators = {
    'x': dec,
}


@decorators['x']
def f(x):
    print(f'hello {x}')


f(1)
