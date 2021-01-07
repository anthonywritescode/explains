import functools


def dec(func):
    @functools.wraps(func)
    def dec_inner(*args, **kwargs):
        print(f'got {args} {kwargs}')
        ret = func(*args, **kwargs)
        print('after')
        return ret
    return dec_inner


def dec2(greeting, farewell):
    def dec2_decorator(func):
        @functools.wraps(func)
        def dec2_inner(*args, **kwargs):
            print(greeting)
            ret = func(*args, **kwargs)
            print(farewell)
            return ret
        return dec2_inner
    return dec2_decorator


@dec2('hello', 'goodbye')
def f(x: int) -> None:
    """this is the docstring"""
    print(f'hello {x}')


class C:
    def __init__(self, x):
        self.x = x

    @property
    def y(self):
        print('in property y')
        return self.x + 5

    @staticmethod
    def func():
        print('normal function')


def main():
    f(1)


if __name__ == '__main__':
    exit(main())
