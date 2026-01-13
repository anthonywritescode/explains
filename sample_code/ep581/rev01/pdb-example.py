def f():
    print('hello world')
    breakpoint()


def main():
    f()


if __name__ == '__main__':
    raise SystemExit(main())
