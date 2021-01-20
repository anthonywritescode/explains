import json
import os.path
import sys


def main() -> int:
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config = json.load(f)
    elif os.path.exists('config.toml'):
        try:
            import toml
        except ImportError:
            sys.stderr.write('need to install toml to use config.toml\n')
            return 1
        else:
            with open('config.toml') as f:
                config = toml.load(f)
    else:
        sys.stderr.write('expected a config.json or config.toml\n')
        return 1

    print(config)


if __name__ == '__main__':
    exit(main())
