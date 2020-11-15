def f():
    try:
        raise KeyboardInterrupt()
    except KeyboardInterrupt:
        pass


def g():
    try:
        raise KeyboardInterrupt
    except KeyboardInterrupt:
        pass


def main():
    try:
        f()
    except KeyboardInterrupt as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    exit(main())
