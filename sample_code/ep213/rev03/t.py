import functools


def dec(x: int):
    print(f'calling dec {x}')

    def dec_decorator(func):
        print(f'calling dec_decorator {x}')

        @functools.wraps(func)
        def dec_inner(*args, **kwargs):
            print(f'calling dec_inner {x}')

            return func(*args, **kwargs)

        return dec_inner

    return dec_decorator


@dec(1)
@dec(2)
@dec(3)
def f(s):
    print(f'inside f: {s}')


f('hello hello world')
