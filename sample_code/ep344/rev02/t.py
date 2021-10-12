import sys


def main() -> int:
    print('hello hello world')
    return 0


print(__name__)
print(sys.modules[__name__])
print(__file__)


if __name__ == '__main__':
    raise SystemExit(main())
