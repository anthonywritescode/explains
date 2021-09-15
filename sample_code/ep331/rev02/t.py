from __future__ import annotations

import argparse
import sys
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    args = parser.parse_args(argv)

    print(f'hello hello {args.name}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
