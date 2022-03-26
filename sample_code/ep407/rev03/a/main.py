import pprint
import sys

pprint.pprint(sys.path)

from b import x


def main() -> int:
    print(f'hello hello world {x=}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
