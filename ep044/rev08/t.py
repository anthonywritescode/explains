import argparse
import pprint
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    # sub-commands
    # subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    status_parser = subparsers.add_parser('status', help='show status')
    status_parser.add_argument('--force', action='store_true')

    checkout_parser = subparsers.add_parser('checkout', help='lots of stuff')
    checkout_parser.add_argument('--verbose', action='count')

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))
    return 0


if __name__ == '__main__':
    exit(main())
