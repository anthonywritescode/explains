import json
import os.path

try:
    import toml
except ImportError:
    toml = None


def main() -> int:
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config = json.load(f)
    elif os.path.exists('config.toml'):
        if toml is None:
            raise SystemExit('need to install toml to use config.toml')
        else:
            with open('config.toml') as f:
                config = toml.load(f)
    else:
        raise SystemExit('expected a config.json or config.toml')

    print(config)


if __name__ == '__main__':
    exit(main())
