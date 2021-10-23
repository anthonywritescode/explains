from __future__ import unicode_literals

import argparse
import os.path


def validate_string(s):
    if not isinstance(s, str):
        raise AssertionError('expected a string, but got {!r}'.format(s))
    return s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', default='.')
    args = parser.parse_args()

    import pdb; pdb.set_trace()
    config_path = os.path.join(args.directory, 'config.yaml')
    validate_string(config_path)
    print('OK! {}'.format(config_path))


if __name__ == '__main__':
    raise SystemExit(main())
