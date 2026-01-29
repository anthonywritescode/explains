import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--hello', help='this is the help for hello')
    parser.parse_args()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
