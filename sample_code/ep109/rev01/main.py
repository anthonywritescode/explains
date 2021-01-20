import json


def main() -> int:
    with open('config.json') as f:
        print(json.load(f))


if __name__ == '__main__':
    exit(main())
