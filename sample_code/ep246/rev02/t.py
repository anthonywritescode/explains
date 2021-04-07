import sys


def hello(name: str) -> None:
    print(f'hello hello {name}')


def main() -> int:
    hello(sys.argv[1])


if __name__ == '__main__':
    exit(main())
