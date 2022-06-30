import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--do-thing', action='store_true')
    parser.add_argument('--no-do-thing', action='store_false', dest='do_thing')
    args = parser.parse_args()
    print(args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
