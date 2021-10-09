import argparse


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--name', required=True)
    parser.add_argument('--noop', action='store_true')
    args = parser.parse_args()

    if not args.noop:
        print(f'hello hello {args.name}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
