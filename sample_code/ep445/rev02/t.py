import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--flag', type=bool)
    args = parser.parse_args()
    print(args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
