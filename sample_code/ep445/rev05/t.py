import argparse


def parse_bool(s: str) -> bool:
    return {'true': True, 'false': False}[s.lower()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--do-thing', action='store_true')
    parser.add_argument('--no-do-thing', action='store_false', dest='do_thing')

    parser.add_argument('--flag', type=parse_bool)

    args = parser.parse_args()
    print(args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
