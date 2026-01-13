import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new-option')
    parser.add_argument('--old-option', deprecated=True)
    args = parser.parse_args()
    assert args


if __name__ == '__main__':
    raise SystemExit(main())
