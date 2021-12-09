import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='count')
    args = parser.parse_args()

    print(f'{args.version=}')

    if args.version:
        print('Python ', end='')
        if args.version >= 2:
            print(sys.version)
        else:
            print(sys.version.split()[0])

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
