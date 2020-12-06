def f():
    raise KeyboardInterrupt()


def g():
    raise KeyboardInterrupt


def main():
    try:
        f()
    except KeyboardInterrupt as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    exit(main())
