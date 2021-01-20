import json
import os.path


def main() -> int:
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config = json.load(f)
    elif os.path.exists('config.toml'):
        try:
            import toml
        except ImportError:
            raise SystemExit('need to install toml to use config.toml')
        else:
            with open('config.toml') as f:
                config = toml.load(f)
    else:
        raise SystemExit('expected a config.json or config.toml')

    print(config)


if __name__ == '__main__':
    exit(main())
