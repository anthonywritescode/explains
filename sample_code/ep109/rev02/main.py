import json
import os.path


def main() -> int:
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config = json.load(f)
    elif os.path.exists('config.toml'):
        ...
    else:
        raise SystemExit('expected a config.json or config.toml')

    print(config)


if __name__ == '__main__':
    exit(main())
