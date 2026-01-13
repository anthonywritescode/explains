def f():
    1 + (3 / 0)


def g():
    f()


def h():
    g()


def main():
    h()


if __name__ == '__main__':
    raise SystemExit(main())
