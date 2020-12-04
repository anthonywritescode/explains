import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-V', '--version',
        action='version',
        version='...',
    )
    args = parser.parse_args(argv)

    return 0


if __name__ == '__main__':
    exit(main())
