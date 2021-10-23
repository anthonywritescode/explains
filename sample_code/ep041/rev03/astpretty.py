import argparse
from typing import Optional
from typing import Sequence

import importlib.metadata


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog='astpretty')
    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {importlib.metadata.version("astpretty")}',
    )
    args = parser.parse_args(argv)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
