import argparse
import sys
from typing import Optional
from typing import Sequence

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog='astpretty')
    parser.add_argument(
        '-V', '--version',
        action='version',
        version=f'%(prog)s {importlib_metadata.version("astpretty")}',
    )
    args = parser.parse_args(argv)

    return 0


if __name__ == '__main__':
    exit(main())
