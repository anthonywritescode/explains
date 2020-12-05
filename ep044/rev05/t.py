import argparse
import pprint
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    # optional
    # - short vs long opts
    # - aliases
    # - defaults
    parser.add_argument(
        '-c', '--config', '--jsonfile',
        default='config.json',
        help='specify the config file. (default: %(default)s)',
    )

    # types
    parser.add_argument(
        '--days',
        # type=int,
    )

    # custom types
    # count
    # append
    # boolean options
    # choices
    # sub-commands

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))
    return 0


if __name__ == '__main__':
    exit(main())
