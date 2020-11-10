def dec(func):
    def dec_inner(*args, **kwargs):
        print(f'got {args} {kwargs}')
        ret = func(*args, **kwargs)
        print('after')
        return ret
    return dec_inner


@dec
def f(x: int) -> None:
    """this is the docstring"""
    print(f'hello {x}')


def main():
    f(1)


if __name__ == '__main__':
    exit(main())
