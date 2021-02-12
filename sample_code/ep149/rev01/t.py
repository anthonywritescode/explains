def f():
    print('f')
    breakpoint()
    return 1


def g():
    print('g')
    f()


def main():
    g()


if __name__ == '__main__':
    exit(main())
