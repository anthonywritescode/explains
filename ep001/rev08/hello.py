import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('person')
    args = parser.parse_args(argv)

    if args.person == '':
        print("Person's name must not be empty!", file=sys.stderr)
        sys.exit(1)

    print(f'Hello Sexy Person {args.person}')


if __name__ == '__main__':
    main()
