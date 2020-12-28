import re
import sys


reg = re.compile('foo (bar)')


def main() -> int:
    match = reg.match(sys.argv[1])
    if match is not None:
        print('matched!')
    else:
        print('not matched')


if __name__ == '__main__':
    exit(main())
