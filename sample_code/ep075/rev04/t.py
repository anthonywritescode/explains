import re
import sys


reg = re.compile('(f)oo (?P<msg>bar)')


def main() -> int:
    match = reg.match(sys.argv[1])
    if match is not None:
        print('matched!')
        breakpoint()
    else:
        print('not matched')


if __name__ == '__main__':
    exit(main())
