#!/usr/bin/env python3
import os.path
import sys


def main() -> int:
    exe = os.path.basename(sys.argv[0])
    if exe == 'uniq':
        seen = {}
        for line in sys.stdin:
            seen[line] = True
        for line in seen:
            print(line, end='')
        return 0
    else:
        raise NotImplementedError(exe)


if __name__ == '__main__':
    raise SystemExit(main())
